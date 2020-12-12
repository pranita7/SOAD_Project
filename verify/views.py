from django.http import HttpResponse
from django.shortcuts import render, redirect
import requests
import urllib.parse
from math import radians, cos, sin, asin, sqrt

def info(request):
    response = requests.get('http://127.0.0.1:8000/alldonatePosts/')
    data = response.json()
    return render(request, 'verify/home.html', {
        'data': data
    })


def distance(lat1, lat2, lon1, lon2):
    # The math module contains a function named
    # radians which converts from degrees to radians.
    lon1 = radians(lon1)
    lon2 = radians(lon2)
    lat1 = radians(lat1)
    lat2 = radians(lat2)

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2

    c = 2 * asin(sqrt(a))

    # Radius of earth in kilometers. Use 3956 for miles
    r = 6371

    # calculate the result
    return (c * r)

def test(request):
    response = requests.get('http://127.0.0.1:8000/alldonatePosts/')
    data = response.json()
    for i in data:
        print(i['is_requested'], i['is_acc_for_transport'])
        if i['is_requested'] == True and (i['is_acc_for_transport'] != True and i['is_acc_for_transport'] != False):
            print('hi')
            url_from = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(i['city']) + '?format=json'
            url_to = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(i['to_city']) + '?format=json'
            response_from = requests.get(url_from).json()
            response_to = requests.get(url_to).json()
            lat1 = float(response_from[0]["lat"])
            lat2 = float(response_to[0]["lat"])
            lon1 = float(response_from[0]["lon"])
            lon2 = float(response_to[0]["lon"])
            dist = distance(lat1, lat2, lon1, lon2)
            dist += (dist/4)
            if(dist<500):
                result = 'true'
            else:
                result = 'false'
            slug = i['slug']+'_'+result
            print(slug)
            url = 'http://127.0.0.1:8000/donatePostEdit/' + slug
            requests.put(url)
    #res = requests.put('http://127.0.0.1:8000/donatePostEdit/donation_true')
    return redirect('info')