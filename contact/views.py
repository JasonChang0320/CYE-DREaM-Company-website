from django.shortcuts import render
from django.views.generic import ListView
from .models import Contact

# Create your views here.

class ContactContentView(ListView):
    model = Contact
    template_name = 'contact.html'
    context_object_name = 'contact_content'