from rest_framework import serializers
from .models import *


class ActorSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='cat.name')
    class Meta:
        model = Actor
        fields = ['title','content','time_create','time_update','cat', 'category_name']
        read_only_fields = ('slug',)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
