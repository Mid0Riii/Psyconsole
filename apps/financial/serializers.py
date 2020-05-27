from rest_framework import serializers
from .models import Order,OrderInc

class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude =["relate_member"]
        read_only_fields=["name",'oid','price','method','exp','date',]

class OrderIncSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrderInc
        exclude =["relate_member"]
        read_only_fields=["name",'oid','price','method','exp','date',]