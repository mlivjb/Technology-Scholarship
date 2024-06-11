from django.shortcuts import HttpResponse, render

from .models import Collection, Story


def index(request):
    context = {
        "collections": [
            {
                "name": collection.name, 
                "href": collection.calculate_href(),
            }
            for collection 
            in Collection.objects.order_by("id")
        ],
    }
    return render(request, f"collections/index.html", context)

def stories(collection_name):
    # look up collection object with a matching name
    collections_stories = Story.objects.filter(collection__name=collection_name)
    def eh(request):
        context = {
            "collection_name": collection_name,
            "stories": [
                {
                    "name": story.name, 
                    "href": story.calculate_href()
                }
                for story 
                in collections_stories.order_by("id")
            ],
        }
        return render(request, f"collections/stories.html", context)
    return eh





# def index(request):
#     context = {}
#     return render(request, "collections/index.html", context)

# def stories(request):
#     context = {}
#     return render(request, "collections/stories.html", context)

# def storyline(request):
#     context = {}
#     return render(request, "collections/stories.html", context)