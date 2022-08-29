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

    def create(self, validated_data):
        return Actor.objects.create(**validated_data)#validated_data появляется после serializer.is_valid(raise_exception=True)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)#.get(пытается получить первый аргумент,если не получается отдает второй)
        instance.content = validated_data.get('content', instance.content)# max_length не обязателен в сериализаторе
        instance.time_create = validated_data.get('time_create', instance.time_create)#read_only=True нужен для указания необязательных полей при POST запросе(они создадутся автоматически)
        instance.time_update = validated_data.get('time_update', instance.time_update)
        instance.cat_id = validated_data.get('cat_id', instance.cat_id)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.save()
        return instance