from rest_framework.views import *
from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.decorators import action


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return Actor.objects.all()
        
        return Actor.objects.filter(pk=pk)

    # @action(methods=['get'], detail=False)#detail определяет возможность использовать pk в url ПЕРЕД category т.е. actors/pk/category
    # def category(self, request, pk = None):
    #     print(self.kwargs)
    #     pk = self.kwargs.get('pk')
    #     if not pk:
    #         categories = Category.objects.all()
    #         return Response({'categories': [i.name for i in categories]})
    #     return Response({'categories': str(Category.objects.get(pk=pk))})


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer