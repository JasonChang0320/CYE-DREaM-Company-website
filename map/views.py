import imp
from django.shortcuts import render
import json
from django.http import JsonResponse,HttpResponseRedirect
from .models import MapPage,MapPage_EN
from .form import VisitorForm

# Create your views here.
def showMapPage(request):
    submit=False
    if request.method == "POST":
        form= VisitorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/MapPage?submit==True")
    else:
        form=VisitorForm
        if "submit" in request.GET:
            submit=True
        MapPage_content=MapPage.objects.all()
    return render(request, 'MapPage.html',{"MapPage_content":MapPage_content,"form":form,"submit":submit})

def showMapPage_EN(request):
    MapPage_content=MapPage.objects.all()
    MapPage_EN_content=MapPage_EN.objects.all()
    zip_MapPage=zip(MapPage_content,MapPage_EN_content)
    return render(request, 'MapPage_EN.html',{"MapPage_content":zip_MapPage})

def grid_dataset(request):
    with open("statics/map.geojson") as f:
        data=json.load(f)

    return JsonResponse(data)

def fault_dataset(request):
    with open("statics/combined_faults.geojson") as f:
        data=json.load(f)

    return JsonResponse(data)