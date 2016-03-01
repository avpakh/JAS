# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import Rivers
from .models import MapFlood
from .models import RiverBasin
from .models import TypeMap
from .models import Probability
from .models import MapImage

def main(request):

    value_option="option1" # first map

    value_damba="no"       # no damba attr

    value_proba1=" " # 0,5proba lists

    value_proba2=" " #  1proba lists

    value_proba3=" " #  5proba lists

    value_proba4=" " #  25proba lists

    value_proba5=" " # 10%

    show_attr="no"

    vis1="0"
    vis2="0"
    vis3="0"
    vis4="0"
    vis5="0"

    riverbasobj=RiverBasin.objects.all()

    typemaps=TypeMap.objects.all()

    probabil=Probability.objects.all()

    maps_list=MapFlood.objects.values_list('description', flat=True).order_by('description')

    print request.POST

    if 'chbox1' in request.POST:
        value_proba1=request.POST['chbox1']

    if 'chbox2' in request.POST:
        value_proba2=request.POST['chbox2']

    if 'chbox3' in request.POST:
        value_proba3=request.POST['chbox3']

    if 'chbox4' in request.POST:
        value_proba4=request.POST['chbox4']

    if 'chbox5' in request.POST:
        value_proba5=request.POST['chbox5']

    if 'damba' in request.POST:
        value_damba= request.POST['damba']

    if 'radioGroup' in request.POST:
        value_option = request.POST['radioGroup']

    if 'river_list' in request.POST:
        selected_value = request.POST['river_list']



        for rivo in riverbasobj:
            if rivo.river_basin == selected_value:
                idrvb=rivo.id_riverbasin


        if value_option=="option1" and value_damba=="no":
            idtype=1

        if value_option=="option1" and value_damba=="yes":
            idtype=3

        if value_option=="option2" and value_damba=="no":
            idtype=2

        if value_option=="option2" and value_damba=="yes":
            idtype=4

        mapso_all=MapImage.objects.all()

        mapso=mapso_all.filter(rvb_index=idrvb,typm_index=idtype)

        list_obj=[]

        if value_proba1=="ch1":
            list_obj.append(value_proba1)
        else:
            list_obj.append("ch1-")
        if value_proba2=="ch2":
            list_obj.append(value_proba2)
        else:
            list_obj.append("ch2-")
        if value_proba3=="ch3":
            list_obj.append(value_proba3)
        else:
            list_obj.append("ch3-")
        if value_proba4=="ch4":
            list_obj.append(value_proba4)
        else:
            list_obj.append("ch4-")

        if value_proba5=="ch5":
            list_obj.append(value_proba5)
        else:
            list_obj.append("ch5-")

        print list_obj

        mapso_count=MapImage.objects.all().filter(rvb_index=idrvb,typm_index=idtype).count()


        proba_m=Probability.objects.all()

        prob_array=[]

        if mapso_count>0:
            show_attr="yes"
            for k in mapso:
                if k.prob_index not in prob_array:
                    prob_array.append(k.prob_index)

            for k_array in proba_m:
                for z_array in prob_array:
                    if k_array.id_probability==z_array.id_probability:
                        if z_array.id_probability==1:
                            vis1 = "1"
                        if z_array.id_probability==2:
                            vis2 = "1"
                        if z_array.id_probability==3:
                            vis3 = "1"
                        if z_array.id_probability==4:
                            vis4 = "1"
                        if z_array.id_probability==5:
                            vis5 = "1"
            print prob_array,value_proba1,value_proba2,value_proba3,value_proba4,value_proba5

            sel_v=[]

            for t in list_obj:
                if t =='ch1':
                    sel_v.append(1)
                if t =='ch2':
                    sel_v.append(2)
                if t =='ch3':
                    sel_v.append(3)
                if t =='ch4':
                    sel_v.append(5)
                if t =='ch5':
                    sel_v.append(4)

            print sel_v
            #if list_obj[0]=='ch1':
            #    k1=mapso.filter(prob_index=1).filter(prob_index=2)
            #if list_obj[1] =='ch2':
            #    k2=k1.filter(prob_index=2)
            #if list_obj[2] == 'ch3':
            #    k3=k2.filter(prob_index=3)


            mapso=mapso.distinct().filter(prob_index__in=sel_v).order_by('part_num')


            print mapso

        return render(request,'maps.html',{'v1':vis1,'v2':vis2,'v3':vis3,'v4':vis4,'v5':vis5,'proba5':value_proba5,'show':show_attr,'proba1':value_proba1,'proba2':value_proba2,'proba3':value_proba3,'proba4':value_proba4,'rivers':riverbasobj,'valdamb':value_damba,'valopt':value_option,'selvalue':selected_value,'typem':typemaps,'proba':probabil,'mapsflood':mapso})

    else:

        return render(request,'maps.html',{'v1':vis1,'v2':vis2,'v3':vis3,'v4':vis4,'v5':vis5,'proba5':value_proba5,'proba1':value_proba1,'proba2':value_proba2,'proba3':value_proba3,'proba4':value_proba4,'rivers':riverbasobj,'typem':typemaps,'proba':probabil,'valopt':value_option,'valdamb':value_damba})

