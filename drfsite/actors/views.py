from rest_framework.views import *
from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.decorators import action
#py drfsite/manage.py runserver

class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return Actor.objects.all()
        
        return Actor.objects.filter(pk=pk)
    
    # def list(self, request):
    #     return Response({'пример': 'П Р И М Е Р'})

    # @action(methods=['get'], detail=False)#detail определяет возможность использовать pk и url ПЕРЕД category т.е. actors/pk/category
    # def category(self, request, pk = None):
    #     categories = Category.objects.all()
    #     return Response({'categories': [i.name for i in categories]})


class CategoryViewSet(viewsets.ModelViewSet):#гораздо проще создать новый вьюсет чем action
    queryset = Category.objects.all()
    serializer_class = CategorySerializer