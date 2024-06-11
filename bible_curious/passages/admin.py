from django.contrib import admin

# Register your models here.
from .models import Collection, Story

admin.site.register(Collection)

admin.site.register(Story)