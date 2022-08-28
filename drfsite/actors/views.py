from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import *
from .models import *


class ActorAPIView(APIView):
    def get(self, request):
        lst = Actor.objects.all().values()#queryset не serializeble нужно values
        return Response({'actors': list(lst)}) 

    def post(self, request):
        new_post = Actor.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id']
        )
        return Response({'post': model_to_dict(new_post)})