from django.shortcuts import render
from rest_framework import generics

from .serializers import ActorSerializer
from .models import *


class ActorAPIView(generics.ListAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer