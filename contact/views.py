from django.shortcuts import render
from django.views.generic import ListView
from .models import Contact, Contact_EN

# Create your views here.

class ContactContentView(ListView):
    model = Contact
    template_name = 'contact.html'
    context_object_name = 'contact_content'

def showContact_EN(request):
    content=Contact_EN.objects.all()
    contact_img=Contact.objects.all()
    return render(request,"contact_EN.html",{"contact_content_EN":content,"contact_content":contact_img})