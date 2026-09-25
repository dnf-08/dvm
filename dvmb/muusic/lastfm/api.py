import requests
from django.conf import settings

base_url = "https://ws.audioscrobbler.com/2.0/"

def topartists(country):
    params={
        'method':'geo.gettopartists',
        'country':country,
        'api_key': settings.LASTFMAPI,
        'format':'json'


    }
    data= requests.get(base_url, params = params)
    return data.json().get('topartists',{}).get('artist',[])

def toptracks(country):
    params={
            'method':'geo.gettoptracks',
            'country':country,
            'api_key':settings.LASTFMAPI,
            'format':'json'
    }
    data= requests.get(base_url, params = params)
    return data.json().get('tracks',{}).get('track',[])


def artistsearch(artist):
    params={
            'method':'artist.search',
            'artist':artist,
            'api_key':settings.LASTFMAPI,
            'format':'json'
    }
    data= requests.get(base_url, params = params)
    return data.json().get('results',{}).get('artistmatches',{}).get('artist',[])
def albumsearch(album):
    params={
            'method':'album.search',
            'album':album,
            'api_key':settings.LASTFMAPI,
            'format':'json'
    }
    data= requests.get(base_url, params = params)
    return data.json().get('results',{}).get('albummatches',{}).get('album',[])

def tracksearch(track):
    params={
            'method':'track.search',
            'track':track,
            'api_key':settings.LASTFMAPI,
            'format':'json'
    }
    data= requests.get(base_url, params = params)
    return data.json().get('results',{}).get('trackmatches',{}).get('track',[])