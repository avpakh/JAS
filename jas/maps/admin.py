from django.contrib import admin

# Register your models here.

from .models import MapFlood


class MapFloodAdmin(admin.ModelAdmin):

	class Meta:
		model = MapFlood


admin.site.register(MapFlood, MapFloodAdmin)