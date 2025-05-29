from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100,required=True)
    email = forms.EmailField(label='Email',required=True)
    message = forms.CharField(label='Message',required=True)


class RegisterForm(forms.ModelForm):
    username = forms.CharField(label='Username', max_length=100 ,required=True )
    email = forms.EmailField(label='Email',required=True)
    password = forms.CharField(label='password',required=True,max_length=100)
    password_confirm = forms.CharField(label='password_confirm',required=True,max_length=100)

    class Meta:
        model = User
        fields = ['username' ,'email' ,'password' ]

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm :
            raise forms.ValidationError("Password do not match")
        

class LoginForm(forms.Form):
    username = forms.CharField(label="username", max_length=100,required=True)
    password = forms.CharField(label="password", max_length=100 , required=True)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        if username and password :
            user = authenticate(username = username , password = password)
            if user is None:
                raise forms.ValidationError(" Invaild username and password")