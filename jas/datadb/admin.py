
# Register your models here.
from .models import DataModel
from .models import Av
from .models import Hour
from .models import AgsStation
from .models import Station
from sorl.thumbnail.admin import AdminImageMixin
from .models import DataAnalys
from .models import GraphData
from .models import RequestAv
from .models import RequestData


from leaflet.admin import LeafletGeoAdmin
from django.contrib import admin

class MyModelAdmin(AdminImageMixin,admin.ModelAdmin):
	pass

class AvAdmin(admin.ModelAdmin):

	class Meta:
		model = Av
	pass

class RequestAvAdmin(admin.ModelAdmin):

	class Meta:
		model = RequestAv
	pass

class RequestDataAdmin(admin.ModelAdmin):

	class Meta:
		model = RequestData
	pass

class StationAdmin(admin.ModelAdmin):

	class Meta:
		model = Station
	pass

class GraphDataAdmin(admin.ModelAdmin):

	class Meta:
		model = GraphData
	pass

class DataAnalysAdmin(admin.ModelAdmin):

	class Meta:
		model = DataAnalys
	pass

class DataHourAdmin(admin.ModelAdmin):

	class Meta:
		model = Hour
	pass


admin.site.register(Av, AvAdmin)
admin.site.register(RequestAv, RequestAvAdmin)
admin.site.register(RequestData, RequestDataAdmin)
admin.site.register(AgsStation, LeafletGeoAdmin)
admin.site.register(Station, StationAdmin)
admin.site.register(DataAnalys,DataAnalysAdmin)
admin.site.register(Hour,DataHourAdmin)
admin.site.register(GraphData,GraphDataAdmin)