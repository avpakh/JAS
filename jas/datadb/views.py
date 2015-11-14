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
from datadb.models import Hour,GraphData
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

def map_page(request):
    ags_spot=AgsStation.objects.all()
    return render(request,'map.html',{'ags_spot':ags_spot})


def graphs_page(request,pk):

    min_level=[]
    max_level=[]

    max_level = GraphData.objects.all().filter(id_station=pk).aggregate(Max('value_avg'))
    min_level = GraphData.objects.all().filter(id_station=pk).aggregate(Min('value_avg'))

    name_ags=''

    station = get_object_or_404(Station, id_station=pk)

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
                  }}],
            chart_options=
               {'chart':
                    {
                    'zoomType': 'x'
                    },
                'title':
                    {
                    'text': 'Уровень,см  '
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

    return render(request,'graphs.html', {'dtchart':cht,'ags':name_ags})

def graph_page(request):

    stations=Station.objects.all()

    return render(request,'graph_basic.html',{'stations':stations})


def table_page(request):

    table = AvTable(Av.objects.all())

    stations=Station.objects.all()

    tableav=False

    RequestConfig(request,paginate={"per_page":10}).configure(table)

    return render(request,'table.html',{'table':table,'stations':stations,'tableav':tableav})

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


     #init_Tables10(request)


def getdata_table10(id_station):
    cnxn = pyodbc.connect("DSN=MSSQL-PYTHON;UID=gmcreader;PWD=123")
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
                where dt> getdate()-10 and mid=1 and id=? and data < 3*?
                group by cast(dt as date)
                order by cast(dt as date) desc
               """,id_station,minlevel)
    rows = cursor.fetchall()
    return rows

def getdata_table5(id_station):
    cnxn = pyodbc.connect("DSN=MSSQL-PYTHON;UID=gmcreader;PWD=123")
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
                where (id = ?) and (mid = 1) and dt>dateadd(day, - 5, getdate()) and data < 3*?
                group by cast(dt as date), datepart(hh, dt)
                ORDER BY Expr1 DESC, Expr2 DESC
               """,id_station,minlevel)
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
    for idsta in stations_id:
        graph5=getdata_table5(idsta)
        for rowdat in graph5:
            datatable5=GraphData()
            datatable5.value_min=rowdat[3]
            datatable5.value_avg=rowdat[2]
            datatable5.value_max=rowdat[4]
            datatable5.date_observation=rowdat[0]
            my_hour=int(rowdat[1])
            my_date=datetime.strptime(rowdat[0], "%Y-%m-%d")
            my_new_date=my_date+timedelta(hours=my_hour)
            datatable5.dt_observation=my_new_date
            datatable5.hour=rowdat[1]
            datatable5.id_station=idsta
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

    return render(request,'table.html',{'stations':stations},)

 #   table = AvTable(Av.objects.all())

 #   table2 = HourTable(Hour.objects.all())

 #   analys_types=DataAnalys.objects.all()

 #    visiblestations=Station.objects.all()

 #   last_date=Av.objects.first()

 #   tableav=True

 #   RequestConfig(request,paginate={"per_page":11}).configure(table)

 #   RequestConfig(request,paginate={"per_page":13}).configure(table2)



