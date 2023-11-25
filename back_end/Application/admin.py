from django.contrib import admin
from .models import *

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
   list_display = ['user']

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
   list_display = ['tabel_number']


@admin.register(Application_Out)
class Application_OutAdmin(admin.ModelAdmin):
   list_display = ['user', 'Basket', 'place']




@admin.register(History_Order)
class History_OrderAdmin(admin.ModelAdmin):
   list_display = ['basket']


# Register your models here.
