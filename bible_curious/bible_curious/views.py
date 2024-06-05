from django.shortcuts import HttpResponse, render

def index(request):
    context = {}
    return render(request, "bible_curious/index.html", context)

def maps(request):
    context = {}
    return render(request, "bible_curious/maps.html", context)

def notes(request):
    context = {}
    return render(request, "bible_curious/notes.html", context)

def verse(request):
    context = {}
    return render(request, "bible_curious/verse_info.html", context)
