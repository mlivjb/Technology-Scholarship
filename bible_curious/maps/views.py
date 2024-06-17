from django.shortcuts import render

from .models import Map


# Create your views here.

def index(request):
    context = {
        "maps": [
            {
                "name": map_collection.name, 
                "href": map_collection.calculate_href(),
                
            }
            for map_collection 
            in Map.objects.order_by("id")
        ],
    }
    return render(request, f"maps/index.html", context)

def map(map_name):
    # look up collection object with a matching name
    maps = Map.objects.filter(name=map_name).first()
    def maps_href(request):
        context = {
            "map_name": map_name,
            "img_name": maps.calculate_href() + ".png"
        }
        return render(request, f"maps/layout_map.html", context)
    return maps_href