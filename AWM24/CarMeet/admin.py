# admin.py

from django.contrib import admin
from .models import Location
from .models import CarMeet

admin.site.register(Location)
admin.site.register(CarMeet)
