from rest_framework import serializers

from .models import Menu, Mahsulot


class MenuSerializers(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'
        

class MahsulotSerializers(serializers.ModelSerializer):
    class Meta:
        model = Mahsulot
        fields = '__all__'