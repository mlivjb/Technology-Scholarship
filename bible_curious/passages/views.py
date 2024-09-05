from django.shortcuts import HttpResponse, render

from .models import Collection, Story, Step

import datetime


def index(request):
    context = {
        "session": request.session.get("user"),
        "collections": [
            {
                "name": collection.name, 
                "href": collection.calculate_href(),
                "page_title": "Collections",
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
            "session": request.session.get("user"),
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
            "session": request.session.get("user"),
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
    story_steps = Step.objects.filter(story__name = story_name).order_by('step_number')
    the_step = story_steps[num - 1]
    def step_href(request):
        context = {
            "session": request.session.get("user"),
            "collection_name": the_step.story.collection.name,
            "collection_href": the_step.story.collection.calculate_href(),
            "story_href": "collections/" + the_step.story.calculate_href(),
            "story_name": story_name,
            "step_number": the_step.step_number,
            "menu_number": "five",
            "menu_href": f"../{story_name}".lower(),
            "next_step": num + 1,
            "prev_step": num - 1,
            "prev_exists": num > 1,
            "next_exists": num < story_steps.count()
        }
        return render(request, f"collections/{story_name}/{num}.html", context)
            
    return step_href

