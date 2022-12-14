"""drfsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import routers

from actors.views import *

router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet)#при отсутствии queryset во view нужно указать basename='name'

urlpatterns = [#закрывать url/
    path('__debug__/', include('debug_toolbar.urls')),
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth/', include('rest_framework.urls')),#cookies авторизация
    path('api/v1/actors/', ActorAPIList.as_view()),
    path('api/v1/actors/<int:pk>/', ActorAPIUpdate.as_view()),
    path('api/v1/actors/delete/<int:pk>/', ActorAPIDestroy.as_view()),
    path(r'api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
] 
urlpatterns += router.urls
