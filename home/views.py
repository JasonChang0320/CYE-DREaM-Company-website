from django.shortcuts import render
from django.http import JsonResponse
import json
import os
from .models import HomePage
from django.views.generic import ListView

# Create your views here.
# def showtemplate(request):
#     return render(request, 'HomePage.html')


# def show_google_map(request):
#     return render(request,"map.html")


class HomePageContentView(ListView):
    model = HomePage
    template_name = 'HomePage.html'
    context_object_name = 'Home_Content'