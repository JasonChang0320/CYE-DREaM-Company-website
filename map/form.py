from django import forms
from django.forms import ModelForm
from .models import Visitor_Info

class VisitorForm(ModelForm):
    class Meta:
        model = Visitor_Info
        fields = ("name","email","job_title")
        labels ={
            "name": "",
            "email": "",
            "job_title": ""
        }
        widgets ={
            "name":forms.TextInput(attrs={"class":"form-control","id":"input_bar","placeholder":"Name"}),
            "email":forms.EmailInput(attrs={"class":"form-control","id":"input_bar","placeholder":"abc@xxx.com"}),
            "job_title":forms.TextInput(attrs={"class":"form-control","id":"input_bar","placeholder":"Affiliation"})
        }