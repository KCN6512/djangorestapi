from rest_framework.views import *
from rest_framework.response import Response
from rest_framework import generics

from .serializers import *
from .models import *

class ActorAPIList(generics.ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorAPIUpdate(generics.UpdateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorCRUDAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class CategoryAPICRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryAPIList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

