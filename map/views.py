import imp
from django.shortcuts import render
import json
from django.http import JsonResponse,HttpResponseRedirect
from .models import MapPage,MapPage_EN
from .form import VisitorForm,VisitorForm_EN
from django.utils.crypto import get_random_string

# Create your views here.
def showMapPage(request):
    submit=False
    token_length=32
    random_token=get_random_string(length=token_length)
    if request.method == "POST":
        form= VisitorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f"/MapPage?{random_token}")
    else:
        form=VisitorForm
        key="100"
        for key in request.GET.keys():
            pass
        if len(key)==token_length:
            submit=True
    MapPage_content=MapPage.objects.all()
    return render(request, 'MapPage.html',{"MapPage_content":MapPage_content,"form":form,"submit":submit,"token":random_token})

def showMapPage_EN(request):
    submit=False
    token_length=32
    random_token=get_random_string(length=32)
    if request.method == "POST":
        form= VisitorForm_EN(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f"/MapPage/en?{random_token}")
    else:
        form=VisitorForm_EN
        key="100"
        for key in request.GET.keys():
            pass
        if len(key)==token_length:
            submit=True
    MapPage_content=MapPage.objects.all()
    MapPage_EN_content=MapPage_EN.objects.all()
    zip_MapPage=zip(MapPage_content,MapPage_EN_content)
    return render(request, 'MapPage_EN.html',{"MapPage_content":zip_MapPage,"form":form,"submit":submit,"token":random_token})

def grid_dataset(request):
    with open("statics/map.geojson") as f:
        data=json.load(f)

    return JsonResponse(data)

def fault_dataset(request):
    with open("statics/combined_faults.geojson") as f:
        data=json.load(f)

    return JsonResponse(data)