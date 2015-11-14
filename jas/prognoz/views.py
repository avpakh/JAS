# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
import os
import pyodbc
from django.conf import settings
from os.path import join
from .models import Maps
from .models import MapsBrovka
from .models import Rivers
from .models import Prognozdata
from .models import Settlements
from .models import MapsData
from .models import Site_New
from .forms import PostLevelForm
from .models import Settlements
from django.shortcuts import get_object_or_404
from math import fabs
from decimal import Decimal
import time
from datetime import datetime,timedelta
from django.utils import timezone
from chartit import DataPool,Chart
from django.db.models import Q



from django.template.context_processors import csrf

# Create your views here.

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core import serializers


def setmap_page(request):
    set_spot=Settlements.objects.all
    print set_spot
    return render(request,'setmap.html',{'set_spot':set_spot})

@api_view(['GET'])
def get_settlements(request):
	result = Settlements.objects.all()
	data = serializers.serialize('json', result)
	return Response(data, status=status.HTTP_200_OK, content_type='application/json')

@api_view(['GET'])
def settlements_filter(request):
	request_data = request.QUERY_PARAMS
	filtered_fields = request_data['fields']

	kwargs = {}

	if "Название населенного пункта" in filtered_fields:
		kwargs['Название населенного пункта'] = request_data['Название населенного пункта']
	if "price" in filtered_fields:
		price = request_data['price'] # e.g (150, 400)
		price_values = price[1:][:-1].split(',')
		min_price = price_values[0]
		max_price = price_values[1]
		kwargs['price__range'] =  (min_price, max_price)
		print kwargs['price__range']
	if "wifi" in filtered_fields:
		kwargs['wifi'] = request_data['wifi']
	if "breakfast" in filtered_fields:
		kwargs['breakfast'] = request_data['breakfast']

	try:
		result = Settlements.objects.filter(**kwargs)
		data = serializers.serialize('json', result)
		return Response(data, status=status.HTTP_200_OK, content_type='application/json')

	except:
		return Response(status=status.HTTP_400_BAD_REQUEST)




def read_file(file_for_reading):

    lists_maps=[]

    while True:
        line=file_for_reading.readline()
        if len(line.rstrip())<25 and len(line.rstrip()) !=0:
            lists_maps.append(line.rstrip())

        if not line: break

    return lists_maps

def create_maps(riverobj,array):

    mymap = Maps.objects.all().filter(river=riverobj)
    l=mymap.count
    if mymap.count()>0:
        Maps.objects.all().filter(river=riverobj).delete()


    for value_str in array:
        map_ind=value_str[7:8]
        level_value=value_str[14:len(value_str)]
        map_obj=Maps()
        map_obj.river=riverobj
        map_obj.map_level=float(level_value)
        map_obj.map_index=map_ind
        map_obj.save()

    return map_obj


def write_level_map():

    # write data from files to Map using

    path=settings.PROJECT_ROOT

    list_rivers=Rivers.objects.all()

    count_map=0

    for myriver in list_rivers:

        file_open=open(join(path,myriver.riverfile))

        list_maps=read_file(file_open)
        count_map=len(list_maps)

        # creat Maps_objects from List_maps
        if Maps.objects.all().filter(river=myriver).count() !=count_map:
            create_maps(myriver,list_maps)

        file_open.close()


    return



def getdata_table1(id_station):
    minlevel=0
    try:
        cnxn = pyodbc.connect("DSN=MSSQL-PYTHON;UID=gmcreader;PWD=123")
        cnxn.autocommit = True
        cursor = cnxn.cursor()
        cursor.execute("""
                select max(data) from dbo._data
                where dt>getdate()-1 and mid=1 and id=?
                group by cast(dt as date)
                order by cast(dt as date) desc
               """,id_station)
        minlev=cursor.fetchall()
        for level in minlev:
            minlevel=level[0]

        cursor = cnxn.cursor()
        cursor.execute("""
                select cast(dt as date) as expr1, datepart(hh, DT) as expr2, avg(data) as expr3,
                min(data) as expr4, max(data)as expr5 from dbo._data
                where (id = ?) and (mid = 1) and dt>dateadd(HOUR ,-2, getdate()) and data < 3*?
                group by cast(dt as date), datepart(hh, dt)
                ORDER BY Expr1 DESC, Expr2 DESC
               """,id_station,minlevel)
        rows = cursor.fetchall()


        return rows
    except:
        return None

def get_name_ags(river_name):

    ags_name=''

    all_riverobj=Rivers.objects.all()

    for rivobj in all_riverobj:
        if rivobj.name == river_name:
            ags_name=rivobj.name_ags

    return ags_name

def get_data_avaliability(river_name):

    data_avaliability=False

    all_riverobj=Rivers.objects.all()

    for rivobj in all_riverobj:
        if rivobj.name == river_name:
            data_avaliability=rivobj.data_avaliable

    return data_avaliability


def get_water_level(river_name):
    water=0
    uroven=0
    res={}
    rivercode=0

    all_riverobj=Rivers.objects.all()

    print river_name

    for rivobj in all_riverobj:
        if rivobj.name == river_name:
            rivercode=rivobj.river_code
            uroven=rivobj.uroven

    print rivercode

    res1=getdata_table1(rivercode)
    if res1 !=None:
        res=res1
        for results in res:
            water=float(uroven)+ float(results[2])/100
        return water
    else:
        water=0
        return water

def main(request):

    write_level_map()

    riverobj=Rivers.objects.all()

    name_ags=''
    water_level=0
    data_aval=True

    if 'river_list' in request.POST:

        selected_value = request.POST['river_list']
        water_level=get_water_level(selected_value)
        name_ags=get_name_ags(selected_value)
        data_aval=get_data_avaliability(selected_value)


    else:
        selected_value = ''
        water_level=0

    return render(request,"prognoz.html",{'rivers':riverobj,'data_aval':data_aval,'selvalue':selected_value,'water_lev':water_level,'nameags':name_ags}, )



def read_write(filename,levelbase,mapid,riverid):

    an_str=''
    analysis=[]

    while True:
        line=filename.readline()
        if len(line.rstrip())<25 and len(line.rstrip()) !=0:
            an_str=line.rstrip()

            if an_str[14:20].rstrip() == str(levelbase):

                print an_str[12:20].rstrip(),levelbase

                z=1
                str_amount=int(an_str[2:6].rstrip())
                print str_amount

                while z<=str_amount:
                    linez=filename.readline()
                    analysis.append(linez)
                    z=z+1


        if not line: break


    print len(analysis)

    print riverid

    riverobj=get_object_or_404(Rivers,pk=riverid)

    mapsobj=get_object_or_404(Maps,pk=mapid)

    prognozobj=Prognozdata.objects.all().filter(map=mapid)

    if prognozobj.count() > 0:
        print 'Not req to add'
    else:
        print prognozobj.count()
        print 'requare to add'

    # select Prognozdata per mapid index

    if prognozobj.count()==0:


        for element in analysis:


            newobj = Prognozdata()
            newobj.river=riverobj
            newobj.map=mapsobj
            #print element
            #print '--------------------------------------------------------------------------------------'
            #print element[2:12],element[13:25],element[26:37],element[46:57],element[74:82],element[84:91]
            newobj.distance=Decimal(element[2:13].rstrip())
            newobj.distance_float=float(element[2:13].rstrip())
            newobj.discharge=Decimal(element[13:25].rstrip())
            newobj.level=Decimal(element[26:37].rstrip())
            newobj.dno=Decimal(element[46:57].rstrip())
            newobj.time100=Decimal(element[74:82].rstrip())
            newobj.brovka=Decimal(element[84:91].rstrip())

            newobj.time60=0

            newobj.save()

    print mapid

    return mapid




def get_map(rivername,level):

    all_riverobj=Rivers.objects.all()

    all_mapsobj=Maps.objects.all()

    mapid=[]
    maplev=[]
    mapmap=[]


    for maps_obj in all_mapsobj:
        for rivobj in all_riverobj:
            if maps_obj.river == rivobj:
                if maps_obj.river.name == rivername:
                    mapid.append(maps_obj.id_maps)
                    maplev.append(maps_obj.map_level)
                    mapmap.append(maps_obj.map_index)

    z=0
    num_level_index=0
    r1=0
    r2=0
    inRange=False
    mapid=0

    print maplev

    while z<len(maplev):


        try:

            if float(level) > float(maplev[z]):
                r1=fabs(float(level)-float(maplev[z]))*fabs(float(level)-float(maplev[z]))
                if z != 1:
                    r2=fabs(float(level)-float(maplev[z-1]))*fabs(float(level)-float(maplev[z-1]))

                    if r1>r2:
                        num_level_index=z-1
                        inRange=True
                        mapid=num_level_index
                        break
                    else:
                        num_level_index=z
                        inRange=True
                        mapid=num_level_index
                        break
                if z == 0:                      # extra value
                    mapid=0
                    inRange=True
                    break

        finally:

            z = z + 1




    if inRange:
        w_level=maplev[mapid]

        return w_level

    else:
        w_level=maplev[z-1]

        return w_level


def put_data_db(rivername,baselevel):


    all_riverobj=Rivers.objects.all()

    all_mapsobj=Maps.objects.all()


    mapid = 0
    idriver=0
    filename=''

    for maps_obj in all_mapsobj:
        for rivobj in all_riverobj:
            if maps_obj.river == rivobj:
                if maps_obj.river.name == rivername and maps_obj.map_level == baselevel:
                    mapid = (maps_obj.id_maps)
                    break

    print mapid

    for rivobj in all_riverobj:
        if rivobj.name == rivername:
            idriver=rivobj.id_river
            filename=rivobj.riverfile
            break

    print idriver,filename

    path=settings.PROJECT_ROOT

    list_rivers=Rivers.objects.all()


    for myriver in list_rivers:

        if myriver.id_river == idriver:

            file_open=open(join(path,myriver.riverfile))

            read_write(file_open,baselevel,mapid,idriver)

            file_open.close()


    return mapid

def results(request):

    riverobj=Rivers.objects.all()

    idriver=0;

    if 'river_list' in request.POST:
        selected_value = request.POST['river_list']


        for rivo in riverobj:
            if rivo.name == selected_value:
                idriver=rivo.id_river


        a_obj=Prognozdata.objects.all().filter(river=idriver)

        riverobjs=get_object_or_404(Rivers,pk=idriver)

        mapdataobj=MapsData.objects.all().filter(river=idriver)

        if mapdataobj.count()==0:

            maps_l = Maps.objects.all().filter(river=idriver)

            for mobj in maps_l:
                mid=mobj.id_maps
                mindex=mobj.map_index
                if mindex==6:
                    a_obj=Prognozdata.objects.all().filter(map=mid)
                    for obj in a_obj:
                        newobj=MapsData()
                        newobj.map_6=obj.discharge
                        newobj.distance_float=obj.distance_float
                        newobj.river=riverobjs
                        newobj.save()

        zzz = MapsData.objects.all().filter(river=idriver)


        ds1=\
            DataPool(
                series=
                [{'options': {
                'source':zzz },
                'terms': [
                'distance_float',
                'map_6',
                'map_1',
                'map_2',
                'map_3',
                'map_4',
                'map_5']}
                 ])

        cht1 = Chart(
                datasource=ds1,
                series_options=
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'distance_float':[
                  'map_6',
                  'map_1',
                  'map_2',
                  'map_3',
                  'map_4',
                  'map_5']
                  }}],
                chart_options=
               {'chart':
                    {
                    'zoomType': 'x',
                      },
                'colors': ['green', 'blue', 'yellow', 'orange', 'red',
                '#f15c80', '#e4d354', '#2b908f', '#f45b5b', '#91e8e1'],
                'title':
                    {
                    'text': ' Расходы реки при различных сценариях весеннего половодья, куб.м/с '
                    },

                 'yAxis':
                    {
                    'title' : {'text': ' куб. м/c '},

                    },

                'xAxis':
                    {
                    'title' : {'text': ' км '},
                    'labels':
                        {'step': 10,  'rotation': 0, 'align': 'bottom'},
                    'minRange': 5,
                    'reversed': 'true'
                    },
                'credits':
                    {
                    'enabled': True
                    },

               },
                x_sortf_mapf_mts=(None,None, False))


        kkk = Site_New.objects.all()

        for zz in kkk:
            print zz.distance,zz.explanation

        dsk=\
            DataPool(
                series=
                [{'options': {
                'source':kkk },
                'terms': [
                'explanation',
                'xaxis']}
                 ])

        cht2 = Chart(
                datasource=dsk,
                series_options=
              [{'options':{
                  'type': 'column',
                  'stacking': False},
                'terms':{
                  'explanation':[
                   'xaxis']
                  }}],
                chart_options=
               {'chart':
                    {
                    'zoomType': 'x',
                      },
                'colors': ['green', 'blue', 'yellow', 'orange', 'red',
                '#f15c80', '#e4d354', '#2b908f', '#f45b5b', '#91e8e1'],
                'title':
                    {
                    'text': ' Уровень превышения воды над бровкой вдоль русла реки Ясельда '
                    },

                'credits':
                    {
                    'enabled': True
                    },

               },
                 x_sortf_mapf_mts=(None,None, False))






        print 'ok'

        return render(request, 'results.html',{'dtchart':cht2,'rivers':riverobj,'selvalue':selected_value})
    else:
        selected_value=''
        print 'out'
        return render(request, 'results.html',{'rivers':riverobj,'selvalue':selected_value,'nograph':'yes'})


def get_level_map(map_id,distance):

     prognoz_obj=Prognozdata.objects.order_by('-distance_float').filter(map=map_id)

     dist_array=[]
     level_array=[]


     for obj in prognoz_obj:
        dist_array.append(obj.distance_float)
        level_array.append(obj.level)

     z=0


     while z<len(dist_array):


        try:

            if float(distance) > float(dist_array[z]):
                r1=fabs(float(distance)-float(dist_array[z]))*fabs(float(distance)-float(dist_array[z]))
                if z != 1:
                    r2=fabs(float(distance)-float(dist_array[z-1]))*fabs(float(distance)-float(dist_array[z-1]))

                    if r1>r2:
                        num_level_index=z-1

                        break
                    else:
                        num_level_index=z

                        break
                if z == 0:                      # extra value

                    break

        finally:

            z = z + 1


     lev = level_array[num_level_index]

     return lev


def post_form_upload(request):

    selected_value=0
    selected_river=''
    selected_ags=''

    if request.method == 'GET':
        form = PostLevelForm()

    else:
        # A POST request: Handle Form Upload
        form = PostLevelForm(request.POST)

        if 'level' in request.POST:
            selected_value = request.POST['level']

        if 'river' in request.POST:
            selected_river = request.POST['river']

        if 'ags' in request.POST:
            selected_ags = request.POST['ags']


       # Find level based on river

        base_level = get_map(selected_river,selected_value)

        print base_level


       # Get array to PrognozData

        map_id = put_data_db(selected_river,base_level)


        print 'map_id',map_id


       # Create Graphs for request

        zzz=Prognozdata.objects.order_by('-distance_float').filter(map=map_id)

        ds=\
            DataPool(
            series=
                [{'options': {
                'source':zzz },
                'terms': [
                'distance',
                'discharge']}
             ])

        cht = Chart(
            datasource=ds,
            series_options=
              [{'options':{
                  'type': 'area',
                  'stacking': False},
                'terms':{
                  'distance': [
                  'discharge']
                  }}],
            chart_options=
               {'chart':
                    {
                    'zoomType': 'x'
                    },
                'title':
                    {
                    'text': 'Расход реки по участку, куб.м/с  '
                    },

                 'yAxis':
                    {
                    'title' : {'text': ' куб.м/с '},

                    },

                'xAxis':
                    {
                    'title' : {'text': ' км '},
                    'labels':
                        {'step': 10,  'rotation': 0, 'align': 'bottom'},
                    'minRange': 5,
                    'reversed': 'true'
                    },
                'credits':
                    {
                    'enabled': True
                    }
               },
           x_sortf_mapf_mts=(None,None, False))


        zzz=Prognozdata.objects.order_by('-distance_float').filter(map=map_id)

        ds0=\
            DataPool(
            series=
                [{'options': {
                'source':zzz },
                'terms': [
                'distance',
                'level']}
             ])

        cht0 = Chart(
            datasource=ds0,
            series_options=
              [{'options':{
                  'type': 'area',
                  'stacking': False},
                'terms':{
                  'distance': [
                  'level']
                  }}],
            chart_options=
               {'chart':
                    {
                    'zoomType': 'x'
                    },
                'title':
                    {
                    'text': ' Расчетный уровень по участку , м '
                    },

                 'yAxis':
                    {
                    'title' : {'text': ' м '},

                    },

                'xAxis':
                    {
                    'title' : {'text': ' км '},
                    'labels':
                        {'step': 10,  'rotation': 0, 'align': 'bottom'},
                    'minRange': 5,
                    'reversed': 'true'
                    },
                'credits':
                    {
                    'enabled': True
                    }
               },
           x_sortf_mapf_mts=(None,None, False))



        zzz=Prognozdata.objects.order_by('-distance_float').filter(map=map_id)




        val = MapsBrovka.objects.all()

        if val.count() > 0:
            MapsBrovka.objects.all().delete()

        for el in zzz:

            mp=MapsBrovka()
            mp.distance_float=el.distance_float
            if el.brovka<0:
                mp.brovka_below=el.brovka
            elif el.brovka>0 and el.brovka< 0.4:
                mp.brovka0_40=el.brovka
            elif el.brovka>=0.4 and el.brovka<1:
                 mp.brovka40_1=el.brovka
            elif el.brovka>=1:
                 mp.brovka1_3=el.brovka
            mp.save()



        zzz = MapsBrovka.objects.all()

        ds1=\
            DataPool(
            series=
                [{'options': {
                'source':zzz },
                'terms': [
                'distance_float',
                'brovka_below',
                'brovka0_40',
                'brovka40_1',
                'brovka1_3']}])
        cht1 = Chart(
            datasource=ds1,
            series_options=
              [{'options':{
                  'type': 'area',
                  'stacking': True},
                'terms':{
                  'distance_float':[
                  'brovka_below',
                  'brovka0_40',
                  'brovka40_1',
                  'brovka1_3' ]
                  }}],
             #  {'options':{
             # 'type': 'line',
             # 'zIndex': 1},
             # 'terms':{
             # 'distance_float': [
             #  'xval']
             # }}],

            chart_options=
               {'chart':
                    {
                    'zoomType': 'x',
                      },
                'colors': ['#058DC7', '#64E572', '#FFF263', '#ED561B', '#8085e9',
                '#f15c80', '#e4d354', '#2b908f', '#f45b5b', '#91e8e1'],
                'title':
                    {
                    'text': ' Превышение над бровкой, м '
                    },

                 'yAxis':
                    {
                    'title' : {'text': ' м '},
                    },

                'xAxis':
                    {
                    'title' : {'text': ' км '},
                    'labels':
                        {'step': 10,  'rotation': 0, 'align': 'bottom'},
                    'minRange': 5,
                    'reversed': 'true'
                    },
                'credits':
                    {
                    'enabled': True
                    },
               },
            x_sortf_mapf_mts = (None, None, False))



        rural=Settlements.objects.all()

        dists=[]
        name_r=[]
        al1=[]
        al2=[]
        dal1=[]
        dal2=[]
        descr1 = " "
        descr2 = " "




        for rural_obj in rural:

            dist_rural_first = rural_obj.start
            dist_rural_end = rural_obj.end

            level_rural_first = rural_obj.start_alarm
            level_rural_end = rural_obj.end_alarm


            name_rural = rural_obj.name

            level_start = get_level_map(map_id,dist_rural_first)
            level_end = get_level_map(map_id,dist_rural_end)

            print dist_rural_first,level_start
            print dist_rural_end,level_end

            value_alarm_first=0
            value_alarm_end=0

            if float(level_start)<float(level_rural_first):
                value_alarm_first=1
                descr1="Нет угрозы затопления"
            elif float(level_start)<float(level_rural_first)+0.4 and float(level_start)>float(level_rural_first):
                value_alarm_first=2
                descr1="угроза затопления территории н.п. до 0.4 м. Низкий риск"
            elif float(level_start)<float(level_rural_first)+1 and float(level_start)>float(level_rural_first)+0.4:
                value_alarm_first=3
                descr1="угроза затопления территории н.п. от 0.4 до 1 м. Повышенный риск"
            elif float(level_start)>float(level_rural_first)+1:
                value_alarm_first=4
                descr1="угроза затопления территории н.п. свыше 1 м. Критический риск"


            if float(level_end)<float(level_rural_end):
                value_alarm_first=1
                descr2="Нет угрозы затопления"
            elif float(level_end)<float(level_rural_end)+0.4 and float(level_end)>float(level_rural_end):
                value_alarm_end=2
                descr2="угроза затопления территории н.п. до 0.4 м. Низкий риск"
            elif float(level_end)<float(level_rural_end)+1 and float(level_end)>float(level_rural_end)+0.4:
                value_alarm_end=3
                descr2="угроза затопления территории н.п. от 0.4 до 1 м. Повышенный риск"

            elif float(level_end)>float(level_rural_end)+1:
                value_alarm_end=4
                descr2="угроза затопления территории н.п. свыше 1 м. Критический риск"



            name_r.append(name_rural)
            dists.append(dist_rural_first)
            al1.append(value_alarm_first)
            al2.append(value_alarm_end)
            dal1.append(descr1)
            dal2.append(descr2)


        t=0

        while t< len(name_r):

            rur_obj = Settlements.objects.get(name=name_r[t])
            if al1[t]>al2[t]:
                rur_obj.alarm=int(al1[t])
                rur_obj.description=dal1[t]
                rur_obj.save()

            if al1[t]<al2[t]:
                rur_obj.alarm=int(al2[t])
                rur_obj.description=dal2[t]
                rur_obj.save()

            if al1[t] == al2[t]:
                rur_obj.alarm=int(al1[t])
                rur_obj.description=dal1[t]
                rur_obj.save()

            t=t+1




         # If data is valid, proceeds to create a new post and redirect the user


        return render(request, 'calc.html', {'dtchart':[cht,cht0,cht1],'form': form ,'levags':selected_value, 'river': selected_river , 'ags': selected_ags  },)


