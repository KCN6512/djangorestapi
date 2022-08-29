from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import *
from .models import *


class ActorAPIView(APIView):
    def get(self, request):
        lst = Actor.objects.all()#queryset не serializeble нужно values
        return Response({'actors': ActorSerializer(lst,many=True).data}) #many=True нужен для бработки списка записей а не одной | .data словарь преобразованных данных

    def post(self, request):
        serializer = ActorSerializer(data=request.data)#нужно указывать data=
        serializer.is_valid(raise_exception=True)#проверка валидности данных чтобы выдавалась ошибка не джанговская желтая, а json форматированная ошибка

        new_post = Actor.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id']
        )
        return Response({'post': ActorSerializer(new_post).data})