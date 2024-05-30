from django.shortcuts import HttpResponse, render

def index(request):
    context = {}
    return render(request, "passages/index.html", context)