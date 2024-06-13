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

    
    # path("leaders_of_the_bible", views.collection_page("stories"), name="stories"),
    # path("leaders_of_the_bible/moses", views.collection_page("storyline"), name="storyline"),
    # path("leaders_of_the_bible/moses/1", views.collection_page("question"), name="question"),
    # path("leaders_of_the_bible/moses/2", views.collection_page("passage"), name="passage"),
    # path("leaders_of_the_bible/moses/3", views.collection_page("games"), name="games"),
