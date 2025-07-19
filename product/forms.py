from django import forms
from django.forms import ModelForm
from .models import Phone

class ProductForm(forms.Form):
    name = forms.CharField(max_length=100, label='Product Name')
    price = forms.IntegerField(label='Price')
    stock = forms.IntegerField(label='Stock')
    description = forms.CharField(widget=forms.Textarea, label='Description')

class PhoneForm(ModelForm):   
    class Meta:
        model = Phone
        fields=["brand","model","price","description","stock"]

    