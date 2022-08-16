import imp
from django.shortcuts import render
import json
from django.http import JsonResponse
from .models import MapPage

# Create your views here.
def showMapPage(request):
    MapPage_content=MapPage.objects.all()
    return render(request, 'MapPage.html',{"MapPage_content":MapPage_content})

def grid_dataset(request):
    with open("statics/map.geojson") as f:
        data=json.load(f)

    return JsonResponse(data)

def fault_dataset(request):
    with open("statics/combined_faults.geojson") as f:
        data=json.load(f)

    return JsonResponse(data)