from dataclasses import fields
import io
from turtle import title
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from .models import *

class ActorModel:
    def __init__(self, title, content) -> None:
        self.title = title
        self.content = content


class ActorSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)#имена переменных сериализатора должны совпадать с именами сериулизуемой модели
    content = serializers.CharField()# max_length не обязателен в сериализаторе


def encode():
    model = ActorModel('Творог','Девятипроцентный творог коровка из кореновки')
    model_serialized = ActorSerializer(model)
    print(model_serialized.data,type(model_serialized.data),sep='\n')
    json = JSONRenderer().render(model_serialized.data)
    print(json)

def decode():
    stream = io.BytesIO(b'{"title": "Tvorog", "content": "Nine percent tvorog korovka iz korenovki"}') 
    data = JSONParser().parse(stream)
    serializer = ActorSerializer(data=data)
    serializer.is_valid()
    print(serializer.validated_data)