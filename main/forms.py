from django import forms

class LoginForm(forms.Form):
    login = forms.CharField(max_length=60,label='login',widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label="password")