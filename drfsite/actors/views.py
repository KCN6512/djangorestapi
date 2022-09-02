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
            return Actor.objects.all()[:5]
        
        return Actor.objects.filter(pk=pk)

    @action(methods=['post'], detail=False)#detail определяет возможность использовать pk и url ПЕРЕД category т.е. actors/pk/category
    def category(self, request):
        categories = Category.objects.all()
        return Response({'categories': [i.name for i in categories]})

    @action(methods=['get'], detail=True)
    def category_detail(self, request, pk=None):
        category_detail = Category.objects.get(pk=pk)
        return Response({'category': category_detail.name})
