# -*- coding: utf-8 -*-
from django.db import models
from sorl.thumbnail import ImageField
from prognoz.models import Rivers

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

