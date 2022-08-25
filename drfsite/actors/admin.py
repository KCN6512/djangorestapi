from django.contrib import admin
from .models import *

class ActorAdmin(admin.ModelAdmin):
    fields = ('title', 'cat', 'content', 'photo')

admin.site.register(Actor,ActorAdmin)
admin.site.register(Category)