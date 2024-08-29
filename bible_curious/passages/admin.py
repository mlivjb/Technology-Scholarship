from django.contrib import admin

# Register your models here.
from .models import Collection, Story, Step, Verse, Personalisation

admin.site.register(Collection)

admin.site.register(Story)

admin.site.register(Step)

admin.site.register(Verse)

admin.site.register(Personalisation)