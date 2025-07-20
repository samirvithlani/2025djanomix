from django import forms
from django.forms import ModelForm
from .models import Phone,Contact

class ProductForm(forms.Form):
    name = forms.CharField(max_length=100, label='Product Name')
    price = forms.IntegerField(label='Price')
    stock = forms.IntegerField(label='Stock')
    description = forms.CharField(widget=forms.Textarea, label='Description')

class PhoneForm(ModelForm):   
    class Meta:
        model = Phone
        fields = ["brand", "model", "price", "description", "stock"]
    
    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise forms.ValidationError("Price must be greater than zero.")
        return price
    
    def clean_stock(self):
        stock = self.cleaned_data.get('stock')
        if stock < 0:
            raise forms.ValidationError("Stock cannot be negative.")
        return stock    

        
class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"

    