from django.shortcuts import render
from App.models import Fertilizer, District_L, Rates, Product
import random
import datetime
import geocoder
import requests

# Create your views here.


def home(request):
    fertilizer = list(Fertilizer.objects.all())
    random.shuffle(fertilizer)
    context = {'fertilizers': fertilizer}
    return render(request, 'App/index.html', context)

def search(request):
    query = request.GET.get('q')
    crops = list(Fertilizer.objects.all())
    random.shuffle(crops)
    if query:
        results = Fertilizer.objects.filter(name__icontains=query)
        rates = Rates.objects.filter(crop__name__icontains=query)
        
        

    else:
        results = []
        rates = []
    context = {'results': results, 'crops': crops, 'query':query, 'rates':rates}

    return render(request, 'App/search.html',context )

def current_weather(api, lat, lon) :
    url = f'http://api.weatherapi.com/v1/current.json?key={api}&q={lat},{lon}'
    response = requests.get(url)
    return response.json()

def latlon(city):
    g = geocoder.osm(city)
    if g.ok:
        return g.latlng
    else:
        print('Error in Fetching Latitude And Longitude!!')

def temp(city):
    api = '4edad4c6c3074567aab71933240904 '
    lat, lon = latlon(city)

    return current_weather(api, lat, lon)




def district(request):

    query = request.GET.get('d')
    
    if query :
        results = District_L.objects.filter(name__icontains=query)
        data = temp(query)
        temperature = data['current']['temp_c']
        condition = data['current']['condition']['text']
        icon = data['current']['condition']['icon']

    else: 
        results =[]
        temperature = ''
        condition = ''
        icon = ''

    return render(request, 'App/district.html', {'results':results, 'temp':temperature, 'condition':condition, 'icon':icon})


def details(request, pk):
    fertilizer = Fertilizer.objects.get(pk=pk)
    
    context = {'fertilizer': fertilizer}
    return render(request, 'App/details.html', context)

def rates(request):
    rates = list(Rates.objects.all())
    random.shuffle(rates)
    context = {'rates':rates}
    return render(request, 'App/rates.html', context)

def products(request):
    product = Product.objects.all()
    context = {'products':product}
    return render(request, 'App/products.html', context)