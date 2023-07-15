from django.contrib import admin
from .models import Airport, Flights, Passenger

# Register your models here.

#optional additional settings for the admin page
class FlightAdmin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration")

#optional additional settings for the admin page
#special way of editing many to many relationships
class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights",)

admin.site.register(Airport)
admin.site.register(Flights, FlightAdmin)
admin.site.register(Passenger, PassengerAdmin)
