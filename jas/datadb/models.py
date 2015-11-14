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
    picture = models.ImageField()

    @property
    def popupContent(self):
      return '<img src="{}"/><p><{}</p>'.format(
           self.picture.url,
           self.description)

    class Meta:
        managed = True
        db_table = u'Agstation'

    def __unicode__(self):
        return u" %s " % (self.description)

    def __str__(self):
        return u" %s " % (self.description)



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


class GraphData(models.Model):
    id_table=models.AutoField(primary_key=True)
    id_station = models.SmallIntegerField('ID_STATION')
    dt_observation=models.DateTimeField('Час/День')
    date_observation = models.DateField('DATA_OBS')
    hour = models.SmallIntegerField('HOUR')  # Field name made lowercase.
    value_min = models.DecimalField('   VALUE_MIN   ',max_digits=6,decimal_places=2)
    value_max = models.DecimalField('   VALUE_MAX   ',max_digits=6,decimal_places=2)
    value_avg = models.DecimalField('   Уровень от отметки 0 станции АГС ',max_digits=6,decimal_places=2)


    class Meta:
        db_table = u'GraphData'

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


