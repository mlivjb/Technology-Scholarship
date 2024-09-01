from django.shortcuts import HttpResponse, render, redirect
from datetime import date, datetime
from passages.models import Verse
from authlib.integrations.django_client import OAuth
from django.conf import settings
from django.urls import reverse
import json
from urllib.parse import quote_plus, urlencode


def index(request):
    this_week = date.today().isocalendar().week
    verse = Verse.objects.filter(week=this_week).first()
    context = {
        "verse": verse,
        "session": request.session.get("user"),
        "pretty": json.dumps(request.session.get("user"), indent=4),
        "domainsee": settings.AUTH0_DOMAIN
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

oauth = OAuth()

oauth.register(
    "auth0",
    client_id=settings.AUTH0_CLIENT_ID,
    client_secret=settings.AUTH0_CLIENT_SECRET,
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f"https://{settings.AUTH0_DOMAIN}/.well-known/openid-configuration",
)

def login(request):
    return oauth.auth0.authorize_redirect(
        request, request.build_absolute_uri(reverse("callback"))
    )
    
def callback(request):
    token = oauth.auth0.authorize_access_token(request)
    request.session["user"] = token
    return redirect(request.build_absolute_uri(reverse("index")))

def logout(request):
    request.session.clear()
    
    return redirect(
        f"https://{settings.AUTH0_DOMAIN}/v2/logout?"
        + urlencode(
            {
                "returnTo": request.build_absolute_uri(reverse("index")),
                "client_id": settings.AUTH0_CLIENT_ID,
            },
            quote_via=quote_plus,
        ),
    )