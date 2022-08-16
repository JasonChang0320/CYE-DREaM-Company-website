from django.shortcuts import render,HttpResponse
from .models import Service,Experience,Service_Title

# Create your views here.
def showtemplate(request):
    return render(request, 'Service.html')

def showService(request):
    title=Service_Title.objects.all()
    service=Service.objects.all()
    experience=Experience.objects.all()
    return render(request,"Service.html",{"service_title":title,"service_content":service,"experience_content":experience})