from rest_framework import serializers
from .models import *


class ActorSerializer(serializers.ModelSerializer):
    slug = serializers.CharField(max_length=255,read_only=True)
    class Meta:
        model = Actor
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'