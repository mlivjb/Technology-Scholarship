from django.urls import path

from . import views
from .models import Collection, Story, Step


urlpatterns = [
    path("", views.index, name="index"),
] + [
    path(collection.calculate_href(), 
    views.stories(collection.name), 
    name=collection.name)
    for collection 
    in Collection.objects.order_by("id")
] + [
    # calculate story path
    path(story.calculate_href(), 
    views.storyline(story.name), 
    name=story.name)
    for story 
    in Story.objects.order_by("id")
] + [
    path(step.calculate_href(), 
    views.step(step.story.name, step.step_number), 
    name=step.name)
    for step 
    in Step.objects.order_by("id")
]
