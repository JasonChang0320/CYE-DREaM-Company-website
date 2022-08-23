from django.shortcuts import render,HttpResponse
from .models import Service,Experience,Service_Title,Service_Title_EN,Service_EN,Experience_EN

# Create your views here.
def showtemplate(request):
    return render(request, 'Service.html')

def showService(request):
    title=Service_Title.objects.all()
    service=Service.objects.all()
    experience=Experience.objects.all()
    return render(request,"Service.html",{"service_title":title,"service_content":service,"experience_content":experience})

def showService_EN(request):
    title=Service_Title.objects.all()
    title_EN=Service_Title_EN.objects.all()
    service=Service.objects.all()
    experience=Experience.objects.all()
    service_EN=Service_EN.objects.all()
    experience_EN=Experience_EN.objects.all()
    zip_title=zip(title,title_EN)
    zip_service=zip(service,service_EN)
    zip_experience=zip(experience,experience_EN)
    return render(request,"Service_EN.html",{"service_title":zip_title,"service_content":zip_service,"experience_content":zip_experience})