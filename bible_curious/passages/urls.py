from django.urls import path

from . import views

urlpatterns = [
    path("", views.collection_page("index"), name="index"),
    path("leaders_of_the_bible", views.collection_page("stories"), name="stories"),
    path("leaders_of_the_bible/moses", views.collection_page("storyline"), name="storyline"),
    path("leaders_of_the_bible/moses/1", views.collection_page("question"), name="question"),
    path("leaders_of_the_bible/moses/2", views.collection_page("passage"), name="passage"),
]