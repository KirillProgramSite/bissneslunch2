from django.contrib import admin
from .models import Review, Menu, Basket, Type

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'overall_rating']


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['name', 'weight', 'price', 'desc', 'calorie', 'protein', 'carbohydrate', 'fat', 'type']
    list_filter = ['type']


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ['user']

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ['name_ru']
