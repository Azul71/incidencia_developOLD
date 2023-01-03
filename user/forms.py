
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser,Departament
from django import forms

from django.contrib import messages
from django.shortcuts import redirect
from user.models import CustomUser
from datetime import datetime
from django.db.models import Count,Sum
from random import randint
from django.core.mail import send_mail
from django.conf import settings

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username','email', 'first_name', 'last_name', 'rol_interno','departament','phone', 'password1', 'password2')
        
       # fields = ('username', 'email','rol_interno','departament')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username','first_name','last_name', 'email','departament')

        widgets={
                   "username":forms.TextInput(attrs={'placeholder':'Enter UserName...','class':'form-control','required':'required'}),
                   "first_name":forms.TextInput(attrs={'placeholder':'Enter Nombre...','class':'form-control','required':'required'}),
                   "last_name":forms.TextInput(attrs={'placeholder':'Enter Apellidos...','class':'form-control','required':'required'}),
                   "email":forms.EmailInput(attrs={'placeholder':'Enter email...','class':'form-control','required':'required'}),
                }  


