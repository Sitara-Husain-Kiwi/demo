from django import forms

class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    middle_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=10)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
