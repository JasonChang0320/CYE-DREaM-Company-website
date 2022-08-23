from django.shortcuts import render
from django.http import JsonResponse
import json
import os
from .models import HomePage,HomePage_EN
from django.views.generic import ListView

# Create your views here.
def showtemplate(request):
    return render(request, 'HomePage_EN.html')

def showHomepage_EN(request):
    content=HomePage_EN.objects.all()
    Home_page_img=HomePage.objects.all()
    return render(request,"HomePage_EN.html",{"Home_Content_EN":content,"Home_Content":Home_page_img})


# def show_google_map(request):
#     return render(request,"map.html")


class HomePageContentView(ListView):
    model = HomePage
    template_name = 'HomePage.html'
    context_object_name = 'Home_Content'