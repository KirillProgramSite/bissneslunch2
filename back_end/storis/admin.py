from django.contrib import admin
from .models import Option, Vote, Stories_Vote_Img, Storis, Storis_img
from .models import Stories_Vote


@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ['title', 'score']

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Stories_Vote_Img)
class Stories_Vote_ImgAdmin(admin.ModelAdmin):
    list_display = ['vote_img']


@admin.register(Storis_img)
class Storis_imgAdmin(admin.ModelAdmin):
    list_display = ['img']


@admin.register(Storis)
class StorisAdmin(admin.ModelAdmin):
    list_display = ['storis']


@admin.register(Stories_Vote)
class Stories_VoteAdmin(admin.ModelAdmin):
   list_display = ['img']



# Register your models here.
