from django.shortcuts import HttpResponse, render

from .models import Collection, Story, Step


def index(request):
    context = {
        "collections": [
            {
                "name": collection.name, 
                "href": collection.calculate_href(),
                "page_title": "zkxchjvgsdjhfgh Collections ",
                "menu_number": "four",
                "menu_href": "/collections"
            }
            for collection 
            in Collection.objects.order_by("id")
        ],
    }
    return render(request, f"collections/index.html", context)

def stories(collection_name):
    # look up collection object with a matching name
    collections_stories = Story.objects.filter(collection__name=collection_name)
    def stories_href(request):
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
    return stories_href

def storyline(story_name): 
    # look up stories object with a matching name
    stories_steps = Step.objects.filter(story__name=story_name)
    def steps_href(request):
        context = {
            "collection_name": stories_steps[0].story.collection.name,
            "collection_href": stories_steps[0].story.collection.calculate_href(),
            "story_name": story_name,
            "steps": [
                {
                    "name": step.name, 
                    "type": step.Step_types(step.type).label,
                    "image": step.Step_types(step.type).label.lower(),
                    "step_number": step.step_number,
                    "href": step.calculate_href()
                }
                for step 
                in stories_steps.order_by("step_number")
            ],
        }
        return render(request, f"collections/storyline.html", context)
    return steps_href

def step(story_name, num): 
    # look up stories object with a matching name
    the_step = Step.objects.filter(step_number = num).filter(story__name = story_name).first()
    def step_href(request):
        context = {
            "collection_name": the_step.story.collection.name,
            "collection_href": the_step.story.collection.calculate_href(),
            "story_href": "collections/" + the_step.story.calculate_href(),
            "story_name": story_name,
            "step_number": the_step.step_number,
            "menu_number": "five",
            "menu_href": f"../{story_name}".lower(),
            "next_step": num + 1
        }
        return render(request, f"collections/{story_name}/{num}.html", context)
    return step_href

def map(request):
    context = {
        "maps": [
            {
                "name": map_collection.name, 
                "href": map_collection.calculate_href(),
                "page_title": "Maps",
                "menu_number": "one",
                "menu_href": "/maps"
            }
            for map_collection 
            in Map.objects.order_by("id")
        ],
    }
    return render(request, f"maps/index.html", context)

def map_image(map_collection):
    # look up collection object with a matching name
    collections_maps = Map.objects.filter(map_collection__name = map_collection)
    def maps_href(request):
        context = {
            "collection_name": map_collection,
            "stories": [
                {
                    "name": map_image.name, 
                    "href": map_image.calculate_href()
                }
                for map_image 
                in collections_maps.order_by("id")
            ],
        }
        return render(request, f"maps/layout_map.html", context)
    return maps_href


# def index(request):
#     context = {}
#     return render(request, "collections/index.html", context)

# def stories(request):
#     context = {}
#     return render(request, "collections/stories.html", context)

# def storyline(request):
#     context = {}
#     return render(request, "collections/stories.html", context)