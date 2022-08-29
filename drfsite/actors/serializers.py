import io
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import *


class ActorSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)#имена переменных сериализатора должны совпадать с именами сериулизуемой модели
    content = serializers.CharField()# max_length не обязателен в сериализаторе
    time_create = serializers.DateTimeField(read_only=True)#read_only=True нужен для указания необязательных полей при POST запросе(они создадутся автоматически)
    time_update = serializers.DateTimeField(read_only=True)
    cat_id = serializers.IntegerField()
    slug = serializers.CharField(max_length=255,read_only=True)
