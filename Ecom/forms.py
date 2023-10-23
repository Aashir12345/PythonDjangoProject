from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms

class CustomerUserform(UserCreationForm):
    username = forms.Charfield(widget = forms.TextInput(attrs=('class':'form-control my-2','paceholder':'Enter Your Name')))
    email = forms.Charfield(widget = forms.TextInput(attrs=('class':'form-control my-2','paceholder':'Enter Your Email')))
    password1 = forms.Charfield(widget = forms.TextInput(attrs=('class':'form-control my-2','paceholder':'Enter Your Password')))
    password2 = forms.Charfield(widget = forms.TextInput(attrs=('class':'form-control my-2','paceholder':'Enter Your Confirm Password')))

    class meta:
        model = User
        fields =['user,email,password1,password2']