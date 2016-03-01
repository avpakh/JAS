# -*- coding: utf-8 -*-
from django.db import models
from sorl.thumbnail import ImageField
from prognoz.models import Rivers

class RiverBasin(models.Model):
    id_riverbasin=models.AutoField(primary_key=True)
    river_basin=models.TextField('Название бассейна реки',max_length=120)

    class Meta:
        managed = True
        db_table = u'RiverBasin'

    def __str__(self):
        return u" %s %s " % (self.id_riverbasin,self.river_basin)

    def __unicode__(self):
        return u" %s %s" % (self.id_riverbasin,self.river_basin)

class TypeMap(models.Model):
    id_typemap=models.AutoField(primary_key=True)
    typemap=models.TextField('Вид карты',max_length=120)

    class Meta:
        managed = True
        db_table = u'TypeMap'

    def __str__(self):
        return u" %s %s " % (self.id_typemap,self.typemap)

    def __unicode__(self):
        return u" %s %s " % (self.id_typemap,self.typemap)

class Probability(models.Model):
    id_probability=models.AutoField(primary_key=True)
    name_probability=models.TextField('Вид обеспеченности',max_length=100)

    class Meta:
        managed = True
        db_table = u'Probability'

    def __str__(self):
        return u" %s %s " % (self.id_probability,self.name_probability)

    def __unicode__(self):
        return u" %s %s " % (self.id_probability,self.name_probability)



class MapImage(models.Model):
    id_mapimage=models.AutoField(primary_key=True)
    rvb_index=models.ForeignKey(RiverBasin)
    typm_index=models.ForeignKey(TypeMap,to_field='id_typemap')
    prob_index=models.ForeignKey(Probability)
    map_image=ImageField(upload_to='/static/im/',blank=True)
    mapcode=models.TextField('Код карты',max_length=10,blank=True)
    mapdescr=models.TextField('Описание карты',max_length=100,blank=True)

    part_num=models.IntegerField(blank=True)

    class Meta:
        managed = True
        db_table = u'MapImage'


class MapFlood(models.Model):
    id_class=models.AutoField(primary_key=True)
    river=models.ForeignKey(Rivers)
    map_index=models.SmallIntegerField('Код карты')
    description=models.TextField('Oписание карты',max_length=120)
    mapflood_image=ImageField(upload_to='maps/static/im/')


    class Meta:
        managed = True
        db_table = u'MapFlood'

    def __str__(self):
        return u" %s %s " % (self.map_index,self.description)

    def __unicode__(self):
        return u" %s %s" % (self.map_index,self.description)

