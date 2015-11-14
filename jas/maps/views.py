# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import Rivers
from .models import MapFlood

def main(request):

    riverobj=Rivers.objects.all()

    maps_list=MapFlood.objects.values_list('description', flat=True).order_by('description')

    if 'river_list' in request.POST:
        selected_value = request.POST['river_list']


        for rivo in riverobj:
            if rivo.name == selected_value:
                idriver=rivo.id_river

        mapso=MapFlood.objects.all().filter(river=idriver)


        return render(request,'maps.html',{'rivers':riverobj,'mapsflood':mapso})
    else:

        return render(request,'maps.html',{'rivers':riverobj})

