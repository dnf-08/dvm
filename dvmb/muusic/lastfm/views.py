from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .api import topartists,toptracks,artistsearch,albumsearch,tracksearch
# Create your views here.
def topartistsv(request):
    country = request.GET.get('country', 'United States')
    artistdic = topartists(country)
    info = {
    'artists': artistdic,
    'country': country,
    }
    return render(request, 'lastfm/topartist.html', info)

def toptracksv(request):
    country = request.GET.get('country', 'United States')
    trackdic = toptracks(country)
    info = {
    'tracks': trackdic,
    'country': country,
    }
    return render(request, 'lastfm/toptrack.html', info)


def artistsearchv(request):
    artist = request.GET.get('artist', 'Radiohead')
    artistdic = artistsearch(artist)
    info = {
    'artists': artistdic,
    'input': artist,
    }
    return render(request, 'lastfm/artistsearch.html', info)


def albumsearchv(request):
    album = request.GET.get('album', 'Nevermind')
    albumdic = albumsearch(album)
    info = {
    'albums': albumdic,
    'input': album,
    }
    return render(request, 'lastfm/albumsearch.html', info)

def tracksearchv(request):
    track = request.GET.get('track', 'Someday')
    trackdic = tracksearch(track)
    info = {
    'tracks': trackdic,
    'input': track,
    }
    return render(request, 'lastfm/tracksearch.html', info)

def home(request):
    return render(request, 'lastfm/home.html')