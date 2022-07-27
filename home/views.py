from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("This is home page")

# Create your views here.
def showtemplate(request):
    return render(request, 'index.html')