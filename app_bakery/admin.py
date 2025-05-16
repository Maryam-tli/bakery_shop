from django.contrib import admin
from app_bakery.models import *

# Register your models here.
class BookingAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'guests', 'date', 'time']
    search_fields = ['name', 'phone', 'email']
    list_filter = ['date',]
    date_hierarchy = 'date'