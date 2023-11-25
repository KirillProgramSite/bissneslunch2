from rest_framework import serializers
from .models import *

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['Id_ru', 'name', 'name_ru']



class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField('get_user_name')

    def get_user_name(self, instance):
        return instance.user.username

    class Meta:
        model = Review
        fields = ['user', 'overall_rating', 'speed_grade', 'taste_grade', 'comment']



class MenuSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField('get_type_name')
    recalls = serializers.SerializerMethodField('get_recalls')

    def get_type_name(self, instance):
        return instance.type.name

    def get_recalls(self, instance):
        recalls = instance.recall.all()
        serializers = ReviewSerializer(recalls, many=True)
        return serializers.data

    class Meta:
        model = Menu
        fields = ['img','name', 'weight', 'price', 'desc', 'calorie', 'protein', 'carbohydrate', 'fat', 'type', 'recalls']

class BasketSerializer(serializers.ModelSerializer):
    eat = serializers.SerializerMethodField('get_menu_name')
    def get_menu_name(self, instance):
        return instance.eat.name

    class Meta:
        model = Basket
        fields = ['user', 'eat']