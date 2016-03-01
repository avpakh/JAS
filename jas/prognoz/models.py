# -*- coding: utf-8 -*-
from django.db import models

from djgeojson.fields import PolygonField
from django.contrib.gis.db import models as gismodels

class Settlements(gismodels.Model):

    name = models.CharField("Название населенного пункта", max_length=50)
    alarm = models.SmallIntegerField("Угроза вначале")
    alarm_end = models.SmallIntegerField("Угроза вконце")
    bereg = models.CharField("Берег", max_length=20)
    start = models.DecimalField("Расстояние по реке Ясельда - начало, км",max_digits=6,decimal_places=2)
    start_brovka = models.DecimalField("Отметка бровки Ясельды - начало, м БС",max_digits=6,decimal_places=2)
    start_alarm = models.DecimalField("Отметка опасности - начало, м БС",max_digits=6,decimal_places=2)
    end = models.DecimalField("Расстояние по реке Ясельда - конец, км",max_digits=6,decimal_places=2)
    end_brovka = models.DecimalField("Отметка бровки Ясельды - конец, м БС",max_digits=6,decimal_places=2)
    end_alarm = models.DecimalField("Отметка опасности - конец, м БС",max_digits=6,decimal_places=2)
    description=models.CharField("Описание риска",max_length=60)

    geom = PolygonField()

    @property
    def popupContent(self):
      return self.alarm,self.name,self.description


    def __unicode__(self):
		return u" %s %s " % (self.name,self.description)




class Rivers(models.Model):
    id_river=models.AutoField(primary_key=True)
    river_code=models.SmallIntegerField('Уникальный код реки')
    name_ags=models.TextField('Название станции',max_length=60)
    name= models.TextField('Название реки')
    riverfile=models.TextField('Файл реки')
    uroven=models.DecimalField('Отметка БС',max_digits=6,decimal_places=2)
    data_avaliable=models.BooleanField('Наличие оперативной информации')

    class Meta:
        managed = True
        db_table = u'Rivers'

    def __str__(self):
        return u" %s %s %s" % (self.id_river,self.name,self.riverfile)

    def __unicode__(self):
        return u" %s %s %s" % (self.id_river,self.name,self.riverfile)

class FloodClassification(models.Model):
    id_class=models.AutoField(primary_key=True)
    map_index=models.SmallIntegerField('Код карты')
    description=models.TextField('Классификация наводнений',max_length=120)

    class Meta:
        managed = True
        db_table = u'FloodClassification'

    def __str__(self):
        return u" %s %s " % (self.map_index,self.description)

    def __unicode__(self):
        return u" %s %s" % (self.map_index,self.description)


class Maps(models.Model):
    id_maps=models.AutoField(primary_key=True)
    river=models.ForeignKey(Rivers)
    map_level=models.DecimalField('Расчетный уровень',max_digits=6,decimal_places=2)
    map_index=models.SmallIntegerField('Код карты')


    class Meta:
        managed = True
        db_table = u'Maps'

class Site_New(models.Model):
    river=models.ForeignKey(Rivers)
    distance=models.FloatField('Расстояние до устья')
    explanation=models.TextField('Объект')
    xaxis =models.SmallIntegerField('z')

    class Meta:
        managed = True
        db_table = u'Site_New'

    def __unicode__(self):
        return u" %s %s " % (self.distance,self.explanation)

    def __str__(self):
        return u" %s %s " % (self.distance,self.explanation)



class MapsBrovka(models.Model):
    distance_float=models.FloatField('Расстояние до устья реки')
    brovka_below=models.DecimalField('Ниже отметки 0 м бровки ',max_digits=5,decimal_places=2,blank=True,null=True)
    brovka0_40=models.DecimalField('От 0  до 40 см превышения над бровкой ',max_digits=5,decimal_places=2,blank=True,null=True)
    brovka40_1=models.DecimalField('От 40 см до 1 м превышения над бровкой',max_digits=5,decimal_places=2,blank=True,null=True)
    brovka1_3=models.DecimalField('Свыше 1м превышения над бровкой',max_digits=5,decimal_places=2,blank=True,null=True)

    class Meta:
        managed = True
        db_table = u'MapsBrovka'


class MapsData(models.Model):
    river=models.ForeignKey(Rivers,blank=True)
    distance_float=models.FloatField('Расстояние до устья реки',blank=True,null=True)
    map_1=models.DecimalField('Высоковероятностный сценарий 25 %ВП (один раз в 4 года)',max_digits=5,decimal_places=2,blank=True,null=True)
    map_2=models.DecimalField('Высоковерояностный сценарий 10% ВП (один раз в 10 лет)',max_digits=5,decimal_places=2,blank=True,null=True)
    map_3=models.DecimalField('Высоковерояностный сценарий 5% ВП (один раз в 20 лет)',max_digits=5,decimal_places=2,blank=True,null=True)
    map_4=models.DecimalField('Низковероятностный сценарий 1% ВП (один раз в 100 лет)', max_digits=5,decimal_places=2,blank=True,null=True)
    map_5=models.DecimalField('Низковерояностный сценарий 0.5% ВП (один раз в 200 лет)',max_digits=5,decimal_places=2,blank=True,null=True)
    map_6=models.DecimalField('Нет существенного затопления',max_digits=5,decimal_places=2,blank=True,null=True)

    class Meta:
        managed = True
        db_table = u'MapsData'


class Prognozdata(models.Model):

    map=models.ForeignKey(Maps)
    river=models.ForeignKey(Rivers)
    distance=models.DecimalField(' Расстояние до устья ' ,max_digits=12,decimal_places=6)
    distance_float=models.FloatField('Расстояние до устья реки')
    discharge=models.DecimalField('Расход реки',max_digits=12,decimal_places=6)
    level=models.DecimalField('Уровень реки',max_digits=12,decimal_places=6)
    dno=models.DecimalField('Отметка дна',max_digits=12,decimal_places=6)
    time60=models.DecimalField('Время в часах:минутах',max_digits=5,decimal_places=2)
    time100=models.DecimalField('Время в часах',max_digits=5,decimal_places=2)
    brovka=models.DecimalField('Превышение над бровкой',max_digits=5,decimal_places=2)

    class Meta:
        managed = True
        db_table = u'PrognozData'

    def __unicode__(self):
        return u" %s %s %s %s %s %s %s %s" % (self.distance_float,self.distance,self.discharge,self.level,self.dno,self.time60,self.time100,self.brovka)

    def __str__(self):
        return u" %s %s %s %s %s %s %s %s" % (self.distance_float,self.distance,self.discharge,self.level,self.dno,self.time60,self.time100,self.brovka)
