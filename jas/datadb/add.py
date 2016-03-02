__author__ = 'alex'

            ags_station = get_object_or_404(AgsStation,station_id=id_station)

            level_zero= ags_station.value_zero
            level_brovka = ags_station.value_brovka


            datatableR=RequestData()
            datatableR.value_min=rowdata[2]/100+level_zero
            datatableR.value_max=rowdata[3]/100+level_zero
            datatableR.date_observation=rowdata[0]
            datatableR.id_station=id_station

            datatableR.value_avg=rowdata[1]/100+level_zero

            temp_value=rowdata[2]/100 + level_zero

            if temp_value < level_brovka:
                datatableR.value_avgBC=temp_value
                datatableR.value_avgBC1=0
                datatableR.value_avgBC2=0
                datatableR.value_avgBC3=0
                datatableR.value_avgBC4=0
                datatableR.value_avgBC50=0
                datatableR.value_avgBC60=temp_value

            if temp_value>=level_brovka and temp_value<(level_brovka+0.5):
                datatableR.value_avgBC1=temp_value
                datatableR.value_avgBC=level_brovka
                datatableR.value_avgBC2=0
                datatableR.value_avgBC3=0
                datatableR.value_avgBC4=0
                datatableR.value_avgBC50=temp_value
                datatableR.value_avgBC60=level_brovka

            if  temp_value >= level_brovka+0.5 and temp_value<(level_brovka+0.8):
                datatableR.value_avgBC2=temp_value
                datatableR.value_avgBC=level_brovka
                datatableR.value_avgBC1=level_brovka+0.5
                datatableR.value_avgBC3=0
                datatableR.value_avgBC4=0
                datatableR.value_avgBC50=level_brovka+0.5
                datatableR.value_avgBC60=level_brovka

            if  temp_value>= level_brovka+0.8 and temp_value<level_brovka + 2:
                datatableR.value_avgBC3=temp_value
                datatableR.value_avgBC=level_brovka
                datatableR.value_avgBC2=level_brovka+0.8
                datatableR.value_avgBC1=level_brovka+0.5
                datatableR.value_avgBC4=0
                datatableR.value_avgBC50=level_brovka+0.5
                datatableR.value_avgBC60=level_brovka

            if  temp_value>=(level_brovka+2):
                datatableR.value_avgBC4=temp_value
                datatableR.value_avgBC=level_brovka
                datatableR.value_avgBC2=level_brovka+0.8
                datatableR.value_avgBC1=level_brovka+0.5
                datatableR.value_avgBC3=level_brovka+2
                datatableR.value_avgBC50=level_brovka+0.5
                datatableR.value_avgBC60=level_brovka

            datatableR.save()