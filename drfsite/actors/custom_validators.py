from rest_framework import serializers


def length_validator(value):
    if len(value) > 50:
        raise serializers.ValidationError