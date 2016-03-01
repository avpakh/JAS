from django.contrib import admin

# Register your models here.

from .models import MapFlood
from .models import RiverBasin
from .models import Probability
from .models import TypeMap
from .models import MapImage

class MapFloodAdmin(admin.ModelAdmin):

	class Meta:
		model = MapFlood

class RiverBasinAdmin(admin.ModelAdmin):

	class Meta:
		model = RiverBasin

class ProbabilityAdmin(admin.ModelAdmin):

	class Meta:
		model = Probability

class TypeMapAdmin(admin.ModelAdmin):

	class Meta:
		model = TypeMap

class MapImageAdmin(admin.ModelAdmin):

	class Meta:
		model = MapImage

admin.site.register(MapFlood, MapFloodAdmin)
admin.site.register(RiverBasin, RiverBasinAdmin)
admin.site.register(Probability, ProbabilityAdmin)
admin.site.register(TypeMap, TypeMapAdmin)
admin.site.register(MapImage, MapImageAdmin)