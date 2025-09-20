from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.models import User

class CustomAuthenticationForm(AuthenticationForm):
    remember_me = forms.BooleanField(required=False,initial=False,label="Remember me")

class CustomeUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)    
    
    class Meta:
        model = User
        fields=("username","email","password1","password2")