from django.shortcuts import render


# Create your views here.
def showtemplate(request):
    return render(request, 'post.html')