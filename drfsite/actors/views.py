from webbrowser import get
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
        serializer.save()#save вызывает create и сохраняет данные в бд
        return Response({'post': serializer.data})#serializer.data ссылается на новый созданный объект

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)

        if not pk:
            return Response({'error': 'Method PUT not allowed'})

        try:
            instance = Actor.objects.get(pk=pk)
        except:
            return Response({'error': 'Object does not exist'})

        serializer = ActorSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data}) 

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)

        if not pk:
            return Response({'error': 'Method DELETE not allowed'})

        try:
            instance = Actor.objects.get(pk=pk)
            instance.delete()
        except:
            return Response({'error': 'Object does not exist'})

        return Response({'deleted': str(instance)})