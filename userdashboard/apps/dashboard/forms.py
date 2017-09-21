from django import forms

class LoginForm(forms.Form):
    email = forms.CharField(label='Email', max_length=255, widget = forms.EmailInput)
    pwd = forms.CharField(label='Password', max_length=255, widget = forms.PasswordInput)
class RegistrationForm(forms.Form):
    first_name = forms.CharField(label="First Name", max_length = 255, widget = forms.TextInput)
    last_name = forms.CharField(label="Last Name", max_length = 255, widget = forms.TextInput)
    email = forms.CharField(label='Email', max_length=255, widget = forms.EmailInput)
    pwd = forms.CharField(label='Password', max_length=255, widget = forms.PasswordInput)