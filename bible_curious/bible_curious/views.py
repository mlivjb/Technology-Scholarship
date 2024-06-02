from django.shortcuts import HttpResponse, render

def index(request):
    context = {}
    return render(request, "bible_curious/index.html", context)