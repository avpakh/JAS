# -*- coding: utf-8 -*-

import django_tables2 as tables
from .models import Hour
from .models import Av

class HourTable(tables.Table):
    hour=tables.Column()
    hour.verbose_name = "Час"
    date_observation=tables.Column()
    date_observation.verbose_name = "Дата"
    value_min=tables.Column()
    value_min.verbose_name = "Минимальное значение, cм"
    value_max=tables.Column()
    value_max.verbose_name = "Максимальное значение, cм"
    value_avg=tables.Column()
    value_avg.verbose_name = "Среднее значение, cм"
    id_station=tables.Column()
    id_station.visible=False
    id_table=tables.Column()
    id_table.visible=False

    class Meta:
        model = Hour
        attrs= {"class":"paleblue"}


class AvTable(tables.Table):
    date_observation=tables.Column()
    date_observation.verbose_name = "Дата"
    value_min=tables.Column()
    value_min.verbose_name = "Минимальное значение, cм"
    value_max=tables.Column()
    value_max.verbose_name = "Максимальное значение, cм"
    value_avg=tables.Column()
    value_avg.verbose_name = "Среднее значение, cм"
    id_station=tables.Column()
    id_station.visible=False
    id_table=tables.Column()
    id_table.visible=False



    class Meta:
        model = Av
        attrs= {"class":"paleblue"}
