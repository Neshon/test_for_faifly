from django.contrib import admin

from .models import Location, Worker, Schedule, Appointment


admin.site.register(Location)
admin.site.register(Worker)
admin.site.register(Schedule)
admin.site.register(Appointment)
