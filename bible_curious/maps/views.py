from django.shortcuts import render

from .models import Map, FavouriteMaps


# Create your views here.

def index(request):
    context = {
        "session": request.session.get("user"),
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
    
    def maps_href(request):
        # look up collection object with a matching name
        maps = Map.objects.filter(name=map_name).first()
        session = request.session.get("user")
        map_is_fav = None
        if session:
            sub = session['userinfo']['sub']
            map_is_fav = FavouriteMaps.objects.filter(user_sub=sub, name=map_name).first()
            if request.method == "POST":
                if map_is_fav:
                    map_is_fav.delete()
                    map_is_fav = None
                else:
                    map_is_fav = FavouriteMaps(user_sub=sub, name=map_name)
                    map_is_fav.save()
        context = {
            "session": request.session.get("user"),
            "map_name": map_name,
            "img_name": maps.calculate_href() + ".png",
            "map_is_fav": ( "checked" if map_is_fav else "")
        }
        return render(request, f"maps/map_layout.html", context)
    return maps_href