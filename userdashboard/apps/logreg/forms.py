from django import forms

class LoginForm(forms.Form):
    email = forms.CharField(label='First name', max_length=255)
    password = forms.CharField(label='Password', max_length=255)