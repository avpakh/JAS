# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Rivers
from .models import Maps
from .models import Prognozdata
from .models import FloodClassification
from .models import MapsBrovka
from .models import MapsData
from .models import Site_New

from .models import Settlements
from leaflet.admin import LeafletGeoAdmin


class RiversAdmin(admin.ModelAdmin):

	class Meta:
		model = Rivers

class MapsAdmin(admin.ModelAdmin):

	list_filter = ['map_index','river']

	class Meta:
		model = Maps

class PrognozDataAdmin(admin.ModelAdmin):

    list_filter = ['map','river']

    class Meta:
		model = Prognozdata

class FloodClassificationAdmin(admin.ModelAdmin):

    class Meta:
		model = FloodClassification

class MapsBrovkaAdmin(admin.ModelAdmin):

    class Meta:
		model = MapsBrovka

class MapsDataAdmin(admin.ModelAdmin):

    class Meta:
		model = MapsData

class Site_NewAdmin(admin.ModelAdmin):

    class Meta:
		model = Site_New

admin.site.register(Rivers, RiversAdmin)
admin.site.register(Settlements,LeafletGeoAdmin)
admin.site.register(Maps,MapsAdmin)
admin.site.register(Prognozdata,PrognozDataAdmin)
admin.site.register(FloodClassification,FloodClassificationAdmin)
admin.site.register(MapsBrovka,MapsBrovkaAdmin)
admin.site.register(MapsData,MapsDataAdmin)
admin.site.register(Site_New,Site_NewAdmin)