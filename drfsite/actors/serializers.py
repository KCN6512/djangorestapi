from dataclasses import fields
from rest_framework import serializers

from .models import Actor


class ActorSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='cat.name')

    class Meta:
        model = Actor
        fields = ('title', 'category_name')