from django.contrib import admin

# Register your models here.
from .models import Collection, Story, Step

admin.site.register(Collection)

admin.site.register(Story)

admin.site.register(Step)