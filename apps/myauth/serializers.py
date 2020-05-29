from .models import CustomUser
from rest_framework import serializers

class CustomUserSerializers(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=('username','password','phone','identity')
    # read_only_fields=['identity']
