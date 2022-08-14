from django.shortcuts import render
import json
from django.http import JsonResponse

# Create your views here.
def showMapPage(request):
    return render(request, 'MapPage.html')

def grid_dataset(request):
    with open("statics/map.geojson") as f:
        data=json.load(f)

    return JsonResponse(data)