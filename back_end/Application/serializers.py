from rest_framework import serializers

from Application.models import *

class TableSerializers(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ('id', 'tabel_number')


class ApplicationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('id', 'user', 'basket', 'delivery_time', 'order_table')



class Application_OutSerializers(serializers.ModelSerializer):
    class Meta:
         model = Application_Out
         fields = ('id', 'user', 'Basket', 'place')



class History_OrderSerializers(serializers.ModelSerializer):
    class Meta:
        models = History_Order
        fields = ('id', 'basket')