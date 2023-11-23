from django.contrib import admin
from .models import Menu, review, Basket

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display =['name']

@admin.register(review)
class reviewAdmin(admin.ModelAdmin):
    list_display = ['comment']

@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ['name']

