from django.contrib import admin
from . models import Country
from . models import TypeLocation
from . models import CityLocality
from . models import LocationLoc 

# Register your models here.
admin.site.register(Country)
admin.site.register(TypeLocation)
admin.site.register(CityLocality)
admin.site.register(LocationLoc)