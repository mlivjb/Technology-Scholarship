from django.shortcuts import HttpResponse, render

from .models import Collection

def collection_page(page_name):
    def response(request):
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
        return render(request, f"collections/{page_name}.html", context)
    return response





# def index(request):
#     context = {}
#     return render(request, "collections/index.html", context)

# def stories(request):
#     context = {}
#     return render(request, "collections/stories.html", context)

# def storyline(request):
#     context = {}
#     return render(request, "collections/stories.html", context)