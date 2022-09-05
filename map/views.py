from django.conf import settings
from django.core.mail import EmailMessage
from django.shortcuts import render
import json
from django.http import JsonResponse,HttpResponseRedirect
from .models import MapPage,MapPage_EN, Visitor_Info
from .form import VisitorForm,VisitorForm_EN
from django.utils.crypto import get_random_string

def send_email(title,content,from_user,to_user):
    email= EmailMessage(
        title,
        content,
        from_user,
        [to_user]
    )
    email.fail_silently = False
    email.send()
    print("Email Send")

# Create your views here.
def showMapPage(request):
    submit=False
    token_length=32
    db_patient_length=5
    random_token=get_random_string(length=token_length)
    cookie_key="LoginCookie"
    if cookie_key in request.COOKIES:
        submit=True
        MapPage_content=MapPage.objects.all()
        return render(request, 'MapPage.html',{"MapPage_content":MapPage_content,"submit":submit,"token":random_token})
    else:
        if request.method == "POST":
            form= VisitorForm(request.POST)
            if form.is_valid():
                form.save()
                response = HttpResponseRedirect(f"/MapPage?{random_token}")
                response.set_cookie("LoginCookie","login",max_age=3600)
                return response
        else:
            form=VisitorForm
            key="100"
            for key in request.GET.keys():
                pass
            if len(key)==token_length:
                submit=True
        MapPage_content=MapPage.objects.all()
        return render(request, 'MapPage.html',{"MapPage_content":MapPage_content,"form":form,"submit":submit,"token":random_token})

def showMapPage_EN(request):
    submit=False
    token_length=32
    random_token=get_random_string(length=32)
    db_patient_length=5
    cookie_key="LoginCookie"
    if cookie_key in request.COOKIES:
        submit=True
        MapPage_content=MapPage.objects.all()
        MapPage_EN_content=MapPage_EN.objects.all()
        zip_MapPage=zip(MapPage_content,MapPage_EN_content)
        return render(request, 'MapPage_EN.html',{"MapPage_content":zip_MapPage,"submit":submit,"token":random_token})
    else:
        if request.method == "POST":
            form= VisitorForm_EN(request.POST)
            if form.is_valid():
                form.save()
                num=len(Visitor_Info.objects.all())
                if num % db_patient_length == 0 and num!=0:
                    try:
                        send_email(title='Django Database 提醒',
                                    content=f"資料庫已有{num}筆資料",
                                    from_user=settings.EMAIL_HOST_USER,
                                    to_user=settings.EMAIL_HOST_USER
                        )
                    except:
                        pass
                return HttpResponseRedirect(f"/MapPage/en?{random_token}")
        else:
            form=VisitorForm_EN
            key="100"
            for key in request.GET.keys():
                pass
            if len(key)==token_length:
                submit=True
        MapPage_content=MapPage.objects.all()
        MapPage_EN_content=MapPage_EN.objects.all()
        zip_MapPage=zip(MapPage_content,MapPage_EN_content)
        return render(request, 'MapPage_EN.html',{"MapPage_content":zip_MapPage,"form":form,"submit":submit,"token":random_token})

def grid_dataset(request):
    with open("statics/map.geojson") as f:
        data=json.load(f)

    return JsonResponse(data)

def fault_dataset(request):
    with open("statics/combined_faults.geojson") as f:
        data=json.load(f)

    return JsonResponse(data)