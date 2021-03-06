# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Booking

# Register your models here.
class BookingAdmin(admin.ModelAdmin):
	model = Booking
	list_display = ('package_Name','contactAddress','contactMobile','contactMail','dateDeparture','dateArrival','duration','totalPersons','adultPersons','childPersons','infantPersons','accomodationType','accomodationStar','modeOfTransport','notes','mealPlan','modePayment')

admin.site.register(Booking,BookingAdmin)
