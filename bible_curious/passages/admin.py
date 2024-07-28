from django.contrib import admin

# Register your models here.
from .models import Collection, Story, Step, Verse

admin.site.register(Collection)

admin.site.register(Story)

admin.site.register(Step)

admin.site.register(Verse)