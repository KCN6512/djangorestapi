from django.db.models import *
from django.db.models.functions import Length
from rest_framework import generics, viewsets
from rest_framework.authentication import *
from rest_framework.decorators import action
from rest_framework.permissions import *
from rest_framework.views import *

from .models import *
from .permissions import IsOwnerOrReadOnly
from .serializers import *


class ActorAPIList(generics.ListCreateAPIView):
    #queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self): #получить queryset напрямую из класса self.queryset нельзя нужно использовать метод
        #is_valid нужен для ДЕсериализации
        #если используется то self.queryset можно не определять
        queryset = Actor.objects.select_related('cat', 'user')
        return queryset

    # def list(self, request):
    #     return Response({'list':self.get_queryset(),'user': str(request.user)}) 
    # #str нужен для сериализации в строку для json


class ActorAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes = [IsOwnerOrReadOnly]
    #authentication_classes = [TokenAuthentication]

class ActorAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes = [IsAdminUser]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @action(detail=True, methods=['get'])
    def func(self, request, pk=None):
        return Response({'pk= ': pk})
    
#     def get_queryset(self):
#         pk = self.kwargs.get('pk')
#         if not pk:
#             return Actor.objects.all()
        
#         return Actor.objects.filter(pk=pk)
    
    # def list(self, request):
    #     return Response({'пример': 'П Р И М Е Р'})

    # @action(methods=['get'], detail=False)#detail определяет возможность использовать pk и url ПЕРЕД category т.е. actors/pk/category
    # def category(self, request, pk = None):
    #     categories = Category.objects.all()
    #     return Response({'categories': [i.name for i in categories]})


# class CategoryViewSet(viewsets.ModelViewSet):#гораздо проще создать новый вьюсет чем action
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

