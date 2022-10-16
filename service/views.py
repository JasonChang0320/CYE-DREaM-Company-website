from django.shortcuts import render,HttpResponse
from .models import *

# Create your views here.
def showtemplate(request):
    return render(request, 'Service.html')

def showService(request):
    title=Service_Title.objects.all()
    service=Service.objects.all()
    return render(request,"Service.html",{"service_title":title,"service_content":service})

def showService_EN(request):
    title=Service_Title.objects.all()
    title_EN=Service_Title_EN.objects.all()
    service=Service.objects.all()
    service_EN=Service_EN.objects.all()
    zip_title=zip(title,title_EN)
    zip_service=zip(service,service_EN)
    return render(request,"Service_EN.html",{"service_title":zip_title,"service_content":zip_service})