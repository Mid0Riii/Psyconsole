from rest_framework import serializers
from .models import Order

class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude =["relate_member"]
        read_only=["name",'oid','price','method','exp','date',]