from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.AviaTicketsInfo)
class AviaTicketsInfoAdmin(admin.ModelAdmin):
    list_display = ('flying_from', 'flying_to', 'price', 'time', 'search_date')
    
@admin.register(models.FlyingFrom)
class FlyingFromAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')
    list_editable = ('status', )
    search_fields = ('name', )
    ordering = ('-status', 'name')
    
@admin.register(models.FlyingTo)
class FlyingToAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')
    list_editable = ('status', )
    search_fields = ('name', )
    ordering = ('-status', 'name')
    