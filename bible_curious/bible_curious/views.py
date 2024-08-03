from django.shortcuts import HttpResponse, render
from datetime import date

from passages.models import Verse

def index(request):
    this_week = date.today().isocalendar().week
    verse = Verse.objects.filter(week=this_week).first()
    context = {
        "verse": verse
    }
    return render(request, "bible_curious/index.html", context)

def maps(request):
    context = {}
    return render(request, "bible_curious/maps.html", context)

def notes(request):
    context = {}
    return render(request, "bible_curious/notes.html", context)

def verse(request):
    this_week = date.today().isocalendar().week
    verse = Verse.objects.filter(week=this_week).first()
    context = {
        "verse": verse
    }
    return render(request, "bible_curious/verse_info.html", context)

def profile(request):
    context = {}
    return render(request, "bible_curious/profile.html", context)