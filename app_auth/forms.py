from django import forms
from .models import *
class LoginForm(forms.Form):

    username = forms.CharField(label="Nom d'utilisateur",widget=forms.TextInput(attrs={"class":"form-control"}))
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput(attrs={"class":"form-control"}))

class RegisterForm(forms.Form):

    username = forms.CharField(label="Nom d'utilisateur",widget=forms.TextInput(attrs={"class":"form-control"}))
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password_confirm = forms.CharField(label="Confirmation", widget=forms.PasswordInput(attrs={"class":"form-control"}))


class ArticleAdminForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={'id':"richtext_field"}))
    class Meta:
        model = Blog
        fields = '__all__'