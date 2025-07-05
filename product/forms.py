from django import forms

class ProductForm(forms.Form):
    name = forms.CharField(max_length=100, label='Product Name')
    price = forms.IntegerField(label='Price')
    stock = forms.IntegerField(label='Stock')
    description = forms.CharField(widget=forms.Textarea, label='Description')
    
    