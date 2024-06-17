from django.urls import path

from . import views
from .models import Map


urlpatterns = [
    path("", views.index, name="index"),
] + [
    path(map.calculate_href(), 
    views.map(map.name), 
    name=map.name)
    for map 
    in Map.objects.order_by("id")
]