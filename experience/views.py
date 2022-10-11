from django.shortcuts import render
from .models import *

# Create your views here.
def showExperience(request):
    title=Experience_Title.objects.all()
    experience=Experience.objects.all()
    NSTC=NSTC_project.objects.all()
    return render(request,"Experience.html",{"experience_title":title,"experience_content":experience,"NSTC_project":NSTC})

def showService_EN(request):
    title=Experience_Title.objects.all()
    title_EN=Experience_Title_EN.objects.all()
    experience=Experience.objects.all()
    experience_EN=Experience_EN.objects.all()
    zip_title=zip(title,title_EN)
    zip_experience=zip(experience,experience_EN)
    return render(request,"Experience_EN.html",{"experience_title":zip_title,"experience_content":zip_experience})