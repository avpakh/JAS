# -*- coding: utf-8 -*-
from django.template import RequestContext

# Create your views here.
import pyodbc
import time

from datetime import datetime,timedelta
from django.utils import timezone
from django.views.generic import ListView
from datadb.models import DataModel
from datadb.models import Av
from datadb.models import RequestAv
from datadb.models import Hour,GraphData,GraphDataBC
from datadb.models import AgsStation
from table import HourTable
from table import AvTable
from django_tables2 import RequestConfig
from datadb.models import Station
from datadb.models import DataAnalys
from chartit import DataPool,Chart
from django.db.models import Max,Min
from django.shortcuts import get_object_or_404


from django.shortcuts import render, render_to_response


def getdata_request(id_station,fromv,tov):

    print type(fromv),id_station,fromv,tov

    dt1 = fromv

    dt2 = tov

    print type(dt1)

    minlevel=0
    try:
        cnxn = pyodbc.connect("DSN=MSSQL-PYTHON;UID=gmcreader;PWD=123",timeout=1)
        cnxn.autocommit = True
        cursor = cnxn.cursor()
        cursor.execute("""
                select min(data) from dbo._data
                where dt>=? and dt<=? and mid=1 and id=?
                group by cast(dt as date)
                order by cast(dt as date) desc
               """,dt1,dt2,id_station)
        minlev=cursor.fetchall()
        for level in minlev:
            minlevel=level[0]


        cursor = cnxn.cursor()
        cursor.execute("""
                select cast (dt as date),avg(data),min(data),max(data) from dbo._data
                where dt>=? and dt<=? and mid=1 and id=? and ((data < 2*?) and (data > ?*0.3))
                group by cast(dt as date)
                order by cast(dt as date) desc
               """,dt1,dt2,id_station,minlevel,minlevel)
        rows = cursor.fetchall()


        # Create a tables from databases
        requestdat = RequestAv.objects.all()
        if requestdat.count()>0:
            RequestAv.objects.all().delete()


        for rowdata in rows:
            data10=RequestAv()
            data10.value_min=rowdata[2]
            data10.value_avg=rowdata[1]
            data10.value_max=rowdata[3]
            data10.date_observation=rowdata[0]
            data10.id_station=id_station
            data10.save()

        return data10

    except:
        return None


def getdata_last(id_station):

    minlevel=0
    try:
        cnxn = pyodbc.connect("DSN=MSSQL-PYTHON;UID=gmcreader;PWD=123",timeout=1)
        cnxn.autocommit = True
        cursor = cnxn.cursor()
        cursor.execute("""
                select min(data) from dbo._data
                where dt>getdate()-1 and mid=1 and id=?
                group by cast(dt as date)
                order by cast(dt as date) desc
               """,id_station)
        minlev=cursor.fetchall()
        for level in minlev:
            minlevel=level[0]

        cursor = cnxn.cursor()
        cursor.execute("""
                select dt,data from dbo._data
                where (id = ?) and (mid = 1) and dt>dateadd(HOUR ,-3, getdate()) and data < 2*? and data > ?*0.3
                ORDER BY dt DESC
               """,id_station,minlevel,minlevel)
        rows = cursor.fetchall()

        cursor = cnxn.cursor()
        cursor.execute("""
                select cast (dt as date),avg(data) from dbo._data
                where (id = ?) and (mid = 1) and dt>dateadd(HOUR ,-3, getdate()) and data < 2*? and data > ?*0.3
                GROUP BY cast(dt as date)
                ORDER BY cast(dt as date) DESC
                """,id_station,minlevel,minlevel)
        rows_av = cursor.fetchall()

        for av_level in rows_av:

            av_data=av_level[1]

        time_list=[]
        data_list=[]

        for level in rows:

            time_list.append(level[0])
            data_list.append(level[1])

        value_last=data_list[-1]
        time_last=time_list[-1]
        value_first=data_list[0]
        time_first=time_list[0]

        level_status=0

        if value_first>av_data:
            level_status=1
        if value_first<av_data:
            level_status=2

        ags=AgsStation.objects.get(station_id=id_station)
        ags.value_level=value_first
        ags.status_level=level_status
        ags.datetime_text=time_first
        ags.value_bc=ags.value_zero+value_first*0.01
        ags.save()

        return rows
    except:
        return None


def request_page(request):

    from_value=''
    to_value=''
    fromv1=''
    tov1=''
    showgr='no'

    index_id=0

    stations=Station.objects.all()

    selected_value=''

    if 'from_' in request.POST:

        from_value=request.POST['from_']

        if from_value == '':
            fromv1=''
        else:
            fromv1='666'

    if 'to_' in request.POST:

        to_value=request.POST['to_']

        if to_value == '':
            tov1=''
        else:
            tov1='666'

    if 'river_list' in request.POST:

        selected_value = request.POST['river_list']


        for k in stations:
            if k.description==selected_value and fromv1=='666' and tov1=='666':
                getdata_request(k.id_station,from_value,to_value)
                index_id=k.id_station

        if  fromv1=='666' and tov1=='666':
            showgr='ok'
        else:
            showgr='no'

        min_level=[]
        max_level=[]

        max_level = RequestAv.objects.all().filter(id_station=index_id).aggregate(Max('value_max'))
        min_level = RequestAv.objects.all().filter(id_station=index_id).aggregate(Min('value_min'))



        ds=\
                    DataPool(
                    series=
                    [{'options': {
                    'source':RequestAv.objects.all().order_by('date_observation') },
                    'terms': [
                    ('date_observation', lambda d: time.mktime(d.timetuple())),
                    'value_avg','value_min','value_max']}
                    ])

        cht = Chart(
                    datasource=ds,
                    series_options=
                [{'options':{
                  'type': 'areaspline',
                  'stacking': False},
                  'terms':{
                  'date_observation': [
                  'value_avg']
                  }},

                    {'options':{
                   'type': 'spline',
                   },
                'terms':{
                  'date_observation': [
                  'value_min','value_max']
                  }},

                ],
        chart_options=
                    {'chart':
                    {
                    'zoomType': 'x'
                    },
                    'title':
                    {
                    'text': 'Измеренный уровень воды, см  ' + ' || станция AГС: '+ selected_value.encode('utf-8')
                    },
                      'colors': ['#34ffff','#349aff','#ff9a34','#ff3434','#35ff34','#9aff34'],

                     'yAxis':
                    {
                    'title' : {'text': ' см '},
                    'min': min_level.values(),
                    'max' :max_level.values(),
                    },
                     'navigation': {
            'buttonOptions': {
                'height': 40,
                'width': 48,
                'symbolSize': 24,
                'symbolX': 23,
                'symbolY': 21,
                'symbolStrokeWidth': 2
            },
                     },

                    'xAxis':
                    {
                    'title' : {'text': ' Дата '},
                    'labels':
                        {'step': 24, 'rotation': 0, 'align': 'bottom'},
                    'minRange': 5
                    },
                    'credits':
                    {
                    'enabled': True
                    },
                    'plotOptions': {
                   'series':

                    {
                     'fillOpacity':1
                    },
                  'spline': {
                  'id':'1',
                  'index':2,
                  'legendIndex':1,
                  'lineWidth': 10,
                  'marker': {
                    'lineWidth': 0,
                    'radius': 0.1,
                    'lineColor': '#666666'

                     },

                  },
                 },
                     'plotOptions': {
                   'series':

                    {
                     'fillOpacity':0.5,

                    },

                  'areaspline': {
                  'id':'0',
                  'index':1,
                  'legendIndex':2,
                  'lineWidth': 0.0,
                  'marker': {
                    'lineWidth': 0.0,
                    'radius': 0.1,
                    'lineColor': '#666666'

                     },

                  },
                 },

                },



        x_sortf_mapf_mts=(None, lambda i: datetime.fromtimestamp(i).strftime(" %Y-%m-%d"), False))





        return render(request,'request.html',{'dtchart':[cht],'stations':stations,'selvalue':selected_value,'showgr':showgr,'fromv':from_value,'tvalue':to_value,'fromv1':fromv1,'tov1':tov1})

    else:

        selected_value=''

        return render(request,'request.html',{'stations':stations,'selvalue':selected_value,'fromv':from_value,'tvalue':to_value,'fromv1':fromv1,'tov1':tov1,'showgr':showgr})




def map_page(request):

    stations_id=[4,7] # list of id_stations

    for idsta in stations_id:

        tt = getdata_last(idsta)

    ags_spot=AgsStation.objects.all()

    return render(request,'map.html',{'ags_spot':ags_spot})


def graphs_page(request,pk):

    min_level=[]
    max_level=[]

    max_level = GraphData.objects.all().filter(id_station=pk).aggregate(Max('value_avg'))
    min_level = GraphData.objects.all().filter(id_station=pk).aggregate(Min('value_avg'))

    name_ags=''

    station = get_object_or_404(Station, id_station=pk)

    ags_station = get_object_or_404(AgsStation,station_id=pk)

    level_zero= ags_station.value_zero

    max_levelBC = float(max_level.values()[0]/100) + level_zero

    val_brovka  = ags_station.value_brovka

    min_levelBC = float(min_level.values()[0]/100) + level_zero

    if min_levelBC> val_brovka:
        min_levelBC=val_brovka-0.005

    stations=Station.objects.all()

    #['#57db15','#f07420','#ffff34','#7cb5ec','#f63535'],

    name_ags=station

    ds=\
            DataPool(
            series=
                [{'options': {
               'source':GraphData.objects.all().order_by('dt_observation').filter(id_station=pk) },
              'terms': [
                ('dt_observation', lambda d: time.mktime(d.timetuple())),
                'value_avg']}
                ])

    cht = Chart(
                datasource=ds,
                series_options=
              [{'options':{
                  'type': 'area',
                  'stacking': False},
                'terms':{
                  'dt_observation': [
                  'value_avg']
                  }}


              ],
                chart_options=
               {'chart':
                    {
                    'zoomType': 'x'
                    },
                'title':
                    {
                    'text': 'Измеренный уровень воды, см  '
                    },

                 'yAxis':
                    {
                    'title' : {'text': ' см '},
                    'min': min_level.values(),
                    'max' :max_level.values(),
                    },

                'xAxis':
                    {
                    'title' : {'text': ' Дата '},
                    'labels':
                        {'step': 24, 'rotation': 0, 'align': 'bottom'},
                    'minRange': 5
                    },
                'credits':
                    {
                    'enabled': True
                    }
               },
                x_sortf_mapf_mts=(None, lambda i: datetime.fromtimestamp(i).strftime("%H:%M %Y-%m-%d"), False))

    ds1=\
            DataPool(
            series=
               [{
                'options': {
               'source':GraphData.objects.all().order_by('dt_observation').filter(id_station=pk) },
              'terms': [
                ('dt_observation', lambda d: time.mktime(d.timetuple())),
                'value_avgBC2','value_avgBC3','value_avgBC4']},
                { 'options': {
               'source':GraphData.objects.all().order_by('dt_observation').filter(id_station=pk) },
              'terms': [
                ('dt_observation', lambda d: time.mktime(d.timetuple())),
                'value_avgBC','value_avgBC1','value_avgBC50']},

                ])

    cht1 = Chart(
                datasource=ds1,
                series_options=
              [


                   {'options':{
                   'type': 'areaspline',
                   },
                'terms':{
                  'dt_observation': [
                  'value_avgBC','value_avgBC2','value_avgBC3','value_avgBC4']
                  }},

                     {'options':{
                   'type': 'line',
                   },
                'terms':{
                  'dt_observation': [
                  'value_avgBC50']
                  }},

                 ],
                chart_options=
               {'chart':
                    {
                    'zoomType': 'x',
                     },

                'title':
                    {
                    'text': 'Измеренный уровень воды в абсолютных отметках БС,м'
                    },

                 'yAxis':
                    {
                    'title' : {'text': ' м '},
                    'min': min_levelBC,
                    'max' :max_levelBC,
                    },

                'xAxis':
                    {
                    'title' : {'text': ' Дата '},
                    'labels':
                        {'step': 24, 'rotation': 0, 'align': 'bottom'},
                    'minRange': 5
                    },
                'colors': ['#ff9a34','#ffff81','#349aff','#ff3434','#35ff34','#9aff34'],

                'credits':
                    {
                    'enabled': True
                    },
                 'legend':
                     {
                      'reversed':'true'
                     },
                    'plotOptions': {
                   'series':

                    {
                     'fillOpacity':1
                    },
                  'line': {
                  'id':'1',
                  'index':2,
                  'legendIndex':1,
                  'lineWidth': 10,
                  'marker': {
                    'lineWidth': 0,
                    'radius': 0,
                    'lineColor': '#666666'

                     },

                  },
                 },
                     'plotOptions': {
                   'series':

                    {
                     'fillOpacity':1,

                    },

                  'areaspline': {
                  'id':'0',
                  'index':1,
                  'legendIndex':2,
                  'lineWidth': 1,
                  'marker': {
                    'lineWidth': 0.0,
                    'radius': 0.0,
                    'lineColor': '#666666'

                     },

                  },
                 },

                },
                x_sortf_mapf_mts=(None, lambda i: datetime.fromtimestamp(i).strftime("%H:%M %Y-%m-%d"), False))


    return render(request,'graphs.html', {'dtchart':[cht,cht1],'ags':name_ags,'stations':stations})



def graph_page(request):

    stations=Station.objects.all()

    return render(request,'graph_basic.html',{'stations':stations})


def table_page(request):

    table = AvTable(Av.objects.all())

    stations=Station.objects.all()

    tableav=True

    RequestConfig(request,paginate={"per_page":10}).configure(table)

    return render(request,'table_basic.html',{'table':table,'stations':stations,'tableav':tableav})

def showdetail(request,pk):

    table = AvTable(Av.objects.all().filter(id_station=pk))

    table2 = HourTable(Hour.objects.all().filter(id_station=pk))

    stations=Station.objects.all()

    analys_types=DataAnalys.objects.all()

    visiblestations=Station.objects.all().filter(id_station=pk)

    last_date=Av.objects.first()

    tableav=True

    RequestConfig(request,paginate={"per_page":11}).configure(table)

    RequestConfig(request,paginate={"per_page":13}).configure(table2)

    return render(request,'table.html',{'table':table,'table2':table2,'stations':stations,'tableav':tableav,'name':visiblestations,'ld':last_date,'analys':analys_types },)


def showtypes(request,pk):

    table = AvTable(Av.objects.all().filter(id_station=pk))

    stations=Station.objects.all()

    visiblestations=Station.objects.all().filter(id_station=pk)

    last_date=Av.objects.first()

    tableav=True

    RequestConfig(request,paginate={"per_page":10}).configure(table)

    return render(request,'table.html',{'table':table,'stations':stations,'tableav':tableav,'name':visiblestations,'ld':last_date},)


     #init_Tables10(request)# Create a tables from databases
    dat10 = Av.objects.all()
    if dat10.count()>0:
        Av.objects.all().delete()

    stations_id=[4,7] # list of id_stations
    for idsta in stations_id:
        row10=getdata_table10(idsta)
        for rowdata in row10:
            datatableav10=Av()
            datatableav10.value_min=rowdata[2]
            datatableav10.value_avg=rowdata[1]
            datatableav10.value_max=rowdata[3]
            datatableav10.date_observation=rowdata[0]
            datatableav10.id_station=idsta
            datatableav10.save()

    return datatableav10


def getdata_table10(id_station):
    cnxn = pyodbc.connect("DSN=MSSQL-PYTHON;UID=gmcreader;PWD=123",timeout=1)
    cnxn.autocommit = True
    cursor = cnxn.cursor()
    cursor.execute("""
                select min(data) from dbo._data
                where dt> getdate()-10 and mid=1 and id=?
                group by cast(dt as date)
                order by cast(dt as date) desc
               """,id_station)
    minlev=cursor.fetchall()
    for level in minlev:
        minlevel=level[0]

    cursor = cnxn.cursor()
    cursor.execute("""
                select cast (dt as date),avg(data),min(data),max(data) from dbo._data
                where dt> getdate()-10 and mid=1 and id=? and data < 2*? and data>0.3*?
                group by cast(dt as date)
                order by cast(dt as date) desc
               """,id_station,minlevel,minlevel)
    rows = cursor.fetchall()
    return rows

def getdata_table5(id_station):
    cnxn = pyodbc.connect("DSN=MSSQL-PYTHON;UID=gmcreader;PWD=123",timeout=1)
    cnxn.autocommit = True
    cursor = cnxn.cursor()
    cursor.execute("""
                select min(data) from dbo._data
                where dt> getdate()-5 and mid=1 and id=?
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
                where (id = ?) and (mid = 1) and dt>dateadd(day, - 5, getdate()) and data < 1.5*? and data > 0.3*?
                group by cast(dt as date), datepart(hh, dt)
                ORDER BY Expr1 DESC, Expr2 DESC
               """,id_station,minlevel,minlevel)
    rows = cursor.fetchall()
    return rows

def init_Tables10(request):

# Create a tables from databases
    dat10 = Av.objects.all()
    if dat10.count()>0:
        Av.objects.all().delete()

    stations_id=[4,7] # list of id_stations
    for idsta in stations_id:
        row10=getdata_table10(idsta)
        for rowdata in row10:
            datatableav10=Av()
            datatableav10.value_min=rowdata[2]
            datatableav10.value_avg=rowdata[1]
            datatableav10.value_max=rowdata[3]
            datatableav10.date_observation=rowdata[0]
            datatableav10.id_station=idsta
            datatableav10.save()

    return datatableav10

def init_Tables5(request):

# Create a tables from databases

    if Hour.objects.all().count()>0:
        Hour.objects.all().delete()

    if GraphData.objects.all().count()>0:
        GraphData.objects.all().delete()

    stations_id=[4,7] # list of id_stations
    for idsta in stations_id:
        row5=getdata_table5(idsta)
        for rowdat in row5:
            datatable5=Hour()
            datatable5.value_min=rowdat[3]
            datatable5.value_avg=rowdat[2]
            datatable5.value_max=rowdat[4]
            datatable5.date_observation=rowdat[0]
            datatable5.hour=rowdat[1]
            datatable5.id_station=idsta
            datatable5.save()

    timezone.now()
    stations_id=[4,7] # list of id_stations

    level_brovka=0
    level_zero=0
    for idsta in stations_id:

        ags_station = get_object_or_404(AgsStation,station_id=idsta)

        level_zero= ags_station.value_zero
        level_brovka = ags_station.value_brovka

        graph5=getdata_table5(idsta)
        for rowdat in graph5:
            datatable5=GraphData()
            datatable5.value_min=rowdat[3]
            datatable5.value_max=rowdat[4]
            datatable5.date_observation=rowdat[0]
            my_hour=int(rowdat[1])

            my_date=datetime.strptime(rowdat[0], "%Y-%m-%d")
            my_new_date=my_date+timedelta(hours=my_hour)

            datatable5.dt_observation=my_new_date
            datatable5.hour=rowdat[1]
            datatable5.id_station=idsta

            datatable5.value_avg=rowdat[2]

            temp_value=rowdat[2]/100 + level_zero

            if temp_value < level_brovka:
                datatable5.value_avgBC=temp_value
                datatable5.value_avgBC1=0
                datatable5.value_avgBC2=0
                datatable5.value_avgBC3=0
                datatable5.value_avgBC4=0
                datatable5.value_avgBC50=0
                datatable5.value_avgBC60=temp_value

            if temp_value>=level_brovka and temp_value<(level_brovka+0.5):
                datatable5.value_avgBC1=temp_value
                datatable5.value_avgBC=level_brovka
                datatable5.value_avgBC2=0
                datatable5.value_avgBC3=0
                datatable5.value_avgBC4=0
                datatable5.value_avgBC50=temp_value
                datatable5.value_avgBC60=level_brovka

            if  temp_value >= level_brovka+0.5 and temp_value<(level_brovka+0.8):
                datatable5.value_avgBC2=temp_value
                datatable5.value_avgBC=level_brovka
                datatable5.value_avgBC1=level_brovka+0.5
                datatable5.value_avgBC3=0
                datatable5.value_avgBC4=0
                datatable5.value_avgBC50=level_brovka+0.5
                datatable5.value_avgBC60=level_brovka

            if  temp_value>= level_brovka+0.8 and temp_value<level_brovka + 2:
                datatable5.value_avgBC3=temp_value
                datatable5.value_avgBC=level_brovka
                datatable5.value_avgBC2=level_brovka+0.8
                datatable5.value_avgBC1=level_brovka+0.5
                datatable5.value_avgBC4=0
                datatable5.value_avgBC50=level_brovka+0.5
                datatable5.value_avgBC60=level_brovka

            if  temp_value>=(level_brovka+2):
                datatable5.value_avgBC4=temp_value
                datatable5.value_avgBC=level_brovka
                datatable5.value_avgBC2=level_brovka+0.8
                datatable5.value_avgBC1=level_brovka+0.5
                datatable5.value_avgBC3=level_brovka+2
                datatable5.value_avgBC50=level_brovka+0.5
                datatable5.value_avgBC60=level_brovka



            datatable5.save()



    return datatable5




class ListStatus(ListView):
    model = DataModel
    template_name = 'get_data.html'

def list_status(request):

    table = HourTable(Hour.objects.all())

    RequestConfig(request,paginate={"per_page":10}).configure(table)

    return render(request,'get_data.html',{'table':table})

def index_view(request):
    template_name = "index.html"

    return render(request, template_name)


def mains(request):
    return render(request,'index.html')


def update_page(request):

    init_Tables10(request)

    init_Tables5(request)

    stations=Station.objects.all()

    return render(request,'graph_basic.html',{'stations':stations},)

 #   table = AvTable(Av.objects.all())

 #   table2 = HourTable(Hour.objects.all())

 #   analys_types=DataAnalys.objects.all()

 #    visiblestations=Station.objects.all()

 #   last_date=Av.objects.first()

 #   tableav=True

 #   RequestConfig(request,paginate={"per_page":11}).configure(table)

 #   RequestConfig(request,paginate={"per_page":13}).configure(table2)



