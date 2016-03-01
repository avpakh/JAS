# -*- coding: utf-8 -*-
from django.db import models
from djgeojson.fields import PointField




class DataAnalys(models.Model):
    id_analys=models.SmallIntegerField('ID_ANALYS')
    analys_type=models.TextField('TYPE')


    class Meta:
        managed = True
        db_table = u'DataAnalys'

    def __unicode__(self):
        return u" %s " % (self.analys_type)

    def __str__(self):
        return u" %s " % (self.analys_type)


class AgsStation(models.Model):
    geom = PointField()
    description = models.TextField()
    description_ru =models.TextField()
    station_id=models.IntegerField()
    value_level=models.DecimalField(max_digits=6,decimal_places=2)
    value_brovka = models.FloatField()
    value_bc=models.DecimalField(max_digits=6,decimal_places=2)
    value_zero=models.FloatField()
    picture = models.ImageField()
    status = models.BooleanField()
    explanation =models.TextField()
    status_level=models.IntegerField() # 1 - level up / 2 - level down
    datetime_text=models.TextField()

    @property
    def popupContent(self):
        if self.status==True and self.status_level==1:
            return '<img src="{}"/><p>{}</p> Данные по уровням воды на  {} <p> <i class="fa fa-level-up fa-1g"> </i> {} см от "0" поста || {} м БС </p> <a href="/datadb/{}"><i class="fa fa-table fa-fw"></i> Таблицы</a> <a href="/datadb/graph/{}"><i class="fa fa-line-chart fa-fw"></i> Графики </a>'.format(
            self.picture.url,
            self.description_ru.encode('utf-8'),
            self.datetime_text,
            self.value_level,
            self.value_bc,
            self.station_id,
            self.station_id)
        if self.status==True and self.status_level==2:
            return '<img src="{}"/><p>{}</p> Данные по уровням воды на {} <p> <i class="fa fa-level-down fa-1g"> </i> {} см от "0" поста || {} м БС </p> <a href="/datadb/{}"><i class="fa fa-table fa-fw"></i> Таблицы</a> <a href="/datadb/graph/{}"><i class="fa fa-line-chart fa-fw"></i> Графики </a>'.format(
            self.picture.url,
            self.description_ru.encode('utf-8'),
            self.datetime_text,
            self.value_level,
            self.value_bc,
            self.station_id,
            self.station_id)
        if self.status==True and self.status_level==0:
            return '<img src="{}"/><p>{}</p> Данные по уровням воды на {} <p> <i class="fa fa-long-arrow-right fa-1g"> </i> {} см от "0" поста || {} м БС </p> <a href="/datadb/{}"><i class="fa fa-table fa-fw"></i> Таблицы</a> <a href="/datadb/graph/{}"><i class="fa fa-line-chart fa-fw"></i> Графики </a>'.format(
            self.picture.url,
            self.description_ru.encode('utf-8'),
            self.datetime_text,
            self.value_level,
            self.value_bc,
            self.station_id,
            self.station_id)

        if self.status==False:
            return '<img src="{}"/><p>{}</p> <p> {} </p>'.format(
            self.picture.url,
            self.description_ru.encode('utf-8'),
            self.explanation.encode('utf-8'))


    class Meta:
        managed = True
        db_table = u'Agstation'

    def __unicode__(self):
        return u" %s %s " % (self.description,self.explanation)



class DataModel(models.Model):
    ids = models.SmallIntegerField('IDS')  # Field name made lowercase.
    dt = models.DateTimeField('DT')  # Field name made lowercase.
    mid = models.SmallIntegerField('MID')  # Field name made lowercase.
    data = models.FloatField('DATA')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '_DATA'

class Station(models.Model):
    id_station=models.SmallIntegerField('ID_STATION')
    description=models.TextField('Description')


    class Meta:
        managed = True
        db_table = u'Station'

    def __unicode__(self):
        return u" %s " % (self.description)

    def __str__(self):
        return u" %s " % (self.description)



class Av(models.Model):
    id_table=models.AutoField(primary_key=True)
    id_station = models.SmallIntegerField('ID_STATION')
    date_observation = models.DateField('  DATA_OBS  ',)  # Field name made lowercase.
    value_min = models.DecimalField('   VALUE_MIN   ',max_digits=6,decimal_places=2)
    value_max = models.DecimalField('   VALUE_MAX   ',max_digits=6,decimal_places=2)
    value_avg = models.DecimalField('   VALUE_AV   ',max_digits=6,decimal_places=2)

    class Meta:
        db_table = u'Av'

    def __unicode__(self):
        return u" %s %s %s %s %s" % (self.id_station,self.date_observation,self.value_min,self.value_max,self.value_avg)


class RequestAv(models.Model):
    id_table=models.AutoField(primary_key=True)
    id_station = models.SmallIntegerField('ID_STATION')
    date_observation = models.DateField('  DATA_OBS  ',)  # Field name made lowercase.
    value_min = models.DecimalField('    Минимальное значение за сутки   ',max_digits=6,decimal_places=2)
    value_max = models.DecimalField('    Максимальное значение за сутки  ',max_digits=6,decimal_places=2)
    value_avg = models.DecimalField('    Уровень от отметки 0 станции АГС (среднее значение за сутки)  ',max_digits=6,decimal_places=2)

    class Meta:
        db_table = u'Request'

    def __unicode__(self):
        return u" %s %s %s %s %s" % (self.id_station,self.date_observation,self.value_min,self.value_max,self.value_avg)


class RequestData(models.Model):
    id_table=models.AutoField(primary_key=True)
    id_station = models.SmallIntegerField('ID_STATION')
    dt_observation=models.DateTimeField('Час/День')
    date_observation = models.DateField('DATA_OBS')
    value_min = models.DecimalField('   Минимальное значение за сутки   ',max_digits=6,decimal_places=2)
    value_max = models.DecimalField('   Максимальное значение за сутки   ',max_digits=6,decimal_places=2)
    value_avg = models.DecimalField('   Уровень от отметки 0 станции АГС (среднее значение за сутки)',max_digits=6,decimal_places=2)
    value_avgBC=models.DecimalField(' Уровень до бровки',null=True,max_digits=6,decimal_places=3)
    value_avgBC1=models.DecimalField('Превышение над бровкой до 50 см',null=True,max_digits=6,decimal_places=3)
    value_avgBC2=models.DecimalField('Превышение над бровкой до 80 см',null=True,max_digits=6,decimal_places=3)
    value_avgBC3=models.DecimalField('Превышение над бровкой до 2 м',null=True,max_digits=6,decimal_places=3)
    value_avgBC4=models.DecimalField('Превышение над бровкой свыше 2 м',null=True,max_digits=6,decimal_places=3)
    value_avgBC50=models.DecimalField('Уровень - 50 см над бровкой',null=True,max_digits=6,decimal_places=3)
    value_avgBC60=models.DecimalField('Уровень до бровки',null=True,max_digits=6,decimal_places=3)

    class Meta:
        db_table = u'RequestData'

    def __unicode__(self):
        return u" %s %s %s %s %s %s %s %s %s %s " % (self.dt_observation,self.date_observation,self.value_min,self.value_max,self.value_avg,self.value_avgBC,self.value_avgBC1,self.value_avgBC2,self.value_avgBC3,self.value_avgBC4)





class GraphData(models.Model):
    id_table=models.AutoField(primary_key=True)
    id_station = models.SmallIntegerField('ID_STATION')
    dt_observation=models.DateTimeField('Час/День')
    date_observation = models.DateField('DATA_OBS')
    hour = models.SmallIntegerField('HOUR')  # Field name made lowercase.
    value_min = models.DecimalField('   VALUE_MIN   ',max_digits=6,decimal_places=2)
    value_max = models.DecimalField('   VALUE_MAX   ',max_digits=6,decimal_places=2)
    value_avg = models.DecimalField('   Уровень от отметки 0 станции АГС ',max_digits=6,decimal_places=2)
    value_avgBC=models.DecimalField(' Уровень до бровки',null=True,max_digits=6,decimal_places=3)
    value_avgBC1=models.DecimalField('Превышение над бровкой до 50 см',null=True,max_digits=6,decimal_places=3)
    value_avgBC2=models.DecimalField('Превышение над бровкой до 80 см',null=True,max_digits=6,decimal_places=3)
    value_avgBC3=models.DecimalField('Превышение над бровкой до 2 м',null=True,max_digits=6,decimal_places=3)
    value_avgBC4=models.DecimalField('Превышение над бровкой свыше 2 м',null=True,max_digits=6,decimal_places=3)
    value_avgBC50=models.DecimalField('Уровень - 50 см над бровкой',null=True,max_digits=6,decimal_places=3)
    value_avgBC60=models.DecimalField('Уровень до бровки',null=True,max_digits=6,decimal_places=3)

    v_1 = models.DecimalField('Уровень до бровки ',null=True,max_digits=6,decimal_places=3)
    v_2 = models.DecimalField('Превышение над бровкой от 0 до 50 см ',null=True,max_digits=6,decimal_places=3)
    v_3 = models.DecimalField('Превышение над бровкой от 50 до 80 см ',null=True,max_digits=6,decimal_places=3)


    class Meta:
        db_table = u'GraphData'

    def __unicode__(self):
        return u" %s %s %s %s %s %s %s %s %s %s %s" % (self.dt_observation,self.date_observation,self.hour,self.value_min,self.value_max,self.value_avg,self.value_avgBC,self.value_avgBC1,self.value_avgBC2,self.value_avgBC3,self.value_avgBC4)

class GraphDataBC(models.Model):
    id_table=models.AutoField(primary_key=True)
    id_station = models.SmallIntegerField('ID_STATION')
    dt_observation=models.DateTimeField('Час/День')
    date_observation = models.DateField('DATA_OBS')
    hour = models.SmallIntegerField('HOUR')  # Field name made lowercase.
    value_min = models.DecimalField('   VALUE_MIN   ',max_digits=6,decimal_places=3)
    value_max = models.DecimalField('   VALUE_MAX   ',max_digits=6,decimal_places=3)
    value_avg = models.DecimalField('   Уровень воды в абсолютных отметках Балтийской системы(БС)',max_digits=6,decimal_places=3)


    class Meta:
        db_table = u'GraphDataBC'

    def __unicode__(self):
        return u" %s %s %s %s %s" % (self.dt_observation,self.date_observation,self.hour,self.value_min,self.value_max,self.value_avg)

    class Meta:
        db_table = u'GraphDataBC'

    def __unicode__(self):
        return u" %s %s %s %s %s" % (self.dt_observation,self.date_observation,self.hour,self.value_min,self.value_max,self.value_avg)


class Hour(models.Model):
    id_table=models.AutoField(primary_key=True)
    id_station = models.SmallIntegerField('ID_STATION')
    date_observation = models.DateField('DATA_OBS')  # Field name made lowercase.
    hour = models.SmallIntegerField('HOUR')  # Field name made lowercase.
    value_min = models.DecimalField('   VALUE_MIN   ',max_digits=6,decimal_places=2)
    value_max = models.DecimalField('   VALUE_MAX   ',max_digits=6,decimal_places=2)
    value_avg = models.DecimalField('   VALUE_AV   ',max_digits=6,decimal_places=2)

    class Meta:
        db_table = u'Hour'

    def __unicode__(self):
        return u" %s %s %s %s %s" % (self.date_observation,self.hour,self.value_min,self.value_max,self.value_avg)


