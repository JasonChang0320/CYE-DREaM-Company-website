from django.shortcuts import render
from .models import AboutContent,Member,AboutContent_EN,Member_EN

# Create your views here.

def showAboutUs(request):
    aboutus_content=AboutContent.objects.all()
    member=Member.objects.all()
    return render(request,"AboutUs.html",{"aboutus_content":aboutus_content,"member_content":member})


def showAboutUs_EN(request):
    aboutus_content=AboutContent.objects.all()
    member=Member.objects.all()
    aboutus_content_EN=AboutContent_EN.objects.all()
    member_EN=Member_EN.objects.all()
    zip_member=zip(member,member_EN)
    return render(request,"AboutUs_EN.html",{"aboutus_content":aboutus_content,\
                                          "aboutus_content_EN":aboutus_content_EN,
                                          "zip_member":zip_member})