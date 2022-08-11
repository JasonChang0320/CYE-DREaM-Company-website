from django.shortcuts import render
from .models import AboutContent,Member

# Create your views here.

def showAboutUs(request):
    aboutus_content=AboutContent.objects.all()
    member=Member.objects.all()
    return render(request,"AboutUs.html",{"aboutus_content":aboutus_content,"member_content":member})