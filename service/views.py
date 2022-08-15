from django.shortcuts import render,HttpResponse
from .models import Service,Experience

# Create your views here.
def showtemplate(request):
    return render(request, 'Service.html')

def showService(request):
    service=Service.objects.all()
    experience=Experience.objects.all()
    return render(request,"Service.html",{"service_content":service,"experience_content":experience})