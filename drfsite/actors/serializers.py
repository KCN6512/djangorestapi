from rest_framework import serializers
from .models import *


class ActorSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='cat.name',required=False)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Actor
        fields = ['id', 'title', 'content', 'time_create', 'time_update', 'cat','slug','category_name','user']
        read_only_fields = ('slug', 'category_name')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
