from urllib import request
from django import forms
from django.contrib.auth import get_user_model
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import ReadOnlyPasswordHashField, AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from accounts.models import *
from PIL import Image
from accounts.options import USERTYPE


# get custom user
User = get_user_model()

class BuyerDetailForm(forms.ModelForm):
    email = forms.EmailField(max_length=100,widget=forms.EmailInput(attrs={
        'class':'form-control ',
        'placeholder':'Email',
        }
    ))
    first_name=forms.CharField(max_length=1200,widget=forms.TextInput(attrs={
    	'class':'form-control',
    	'placeholder':'Ad',
        'autofocus': '',
    	}))
    last_name=forms.CharField(max_length=1200,widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Soyad'
        }))

    birthday=forms.CharField(required=False,widget=forms.DateInput(attrs={
        'class': 'form-control',
        'type':'date'
        
    	}))

    phone_number = forms.CharField(required=False,widget=forms.TextInput(attrs={
        'type':'number'
        }))

    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class':'form-control'
    }))

    usertype = forms.CharField(widget=forms.Select(choices=USERTYPE,attrs={
        'class':'form-control'
    }))
    
    
    # phone_number=
    # password1=forms.CharField(max_length=100,widget=forms.PasswordInput(
    #     attrs={
    #     'class':'form-control',
    #     'placeholder':'Şifrə'
    #     }
    # ))
    # password2=forms.CharField(max_length=100,widget=forms.PasswordInput(
    #     attrs={
    #     'class':'form-control',
    #     'placeholder':'Şifrəni doğrula'
    #     }
    # ))


    class Meta:
        model = User
        fields = ('first_name','birthday','last_name','email','phone_number','image','usertype')







class SellerDetailForm(forms.ModelForm):
    email = forms.EmailField(max_length=100,widget=forms.EmailInput(attrs={
        'class':'form-control ',
        'placeholder':'Email',
        }
    ))
    first_name=forms.CharField(max_length=1200,widget=forms.TextInput(attrs={
    	'class':'form-control',
    	'placeholder':'Ad',
        'autofocus': '',
    	}))
    last_name=forms.CharField(max_length=1200,widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Soyad'
        }))

    birthday=forms.CharField(required=False,widget=forms.DateInput(attrs={
        'class': 'form-control',
        'type':'date'
        
    	}))

    phone_number = forms.CharField(required=False,widget=forms.TextInput(attrs={
        'type':'number'
        }))

    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class':'form-control'
    }))

    company_name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control'
    }))

    usertype = forms.CharField(widget=forms.Select(choices=USERTYPE,attrs={
        'class':'form-control'
    }))
    
    # phone_number=
    # password1=forms.CharField(max_length=100,widget=forms.PasswordInput(
    #     attrs={
    #     'class':'form-control',
    #     'placeholder':'Şifrə'
    #     }
    # ))
    # password2=forms.CharField(max_length=100,widget=forms.PasswordInput(
    #     attrs={
    #     'class':'form-control',
    #     'placeholder':'Şifrəni doğrula'
    #     }
    # ))


    class Meta:
        model = User
        fields = ('first_name','birthday','last_name','email','phone_number','image','usertype','company_name')
