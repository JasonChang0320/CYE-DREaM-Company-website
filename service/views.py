from django.shortcuts import render,HttpResponse

# Create your views here.
def showtemplate(request):
    return render(request, 'Service.html')