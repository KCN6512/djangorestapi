from rest_framework import serializers
from .models import *
from .custom_validators import *


class ActorSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='cat.name',read_only=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    creator_user = serializers.CharField(source='user.username', read_only=True)
    title = serializers.CharField(validators=[length_validator])


    class Meta:
        model = Actor
        fields = ['id', 'title', 'content', 'time_create', 'time_update', 'cat',
        'slug', 'category_name', 'user', 'creator_user']
        read_only_fields = ('slug', 'category_name')


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


# Validators
# Individual fields on a serializer can include validators, 
# by declaring them on the field instance, for example:

# def multiple_of_ten(value):
#     if value % 10 != 0:
#         raise serializers.ValidationError('Not a multiple of ten')

# class GameRecord(serializers.Serializer):
#     score = IntegerField(validators=[multiple_of_ten])
#     ...