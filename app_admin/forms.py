from django import forms
from .models import *

class CommentForm(forms.ModelForm):
    class Meta:

        model =Comment
        fields = ['content', 'name_post']
        labels = {'content':'Commentaire', 'name_post':'Nom & Prenom'}
        widgets = {
            'name_post':forms.TextInput(attrs={'class':'form-control'}),
            'content':forms.Textarea(attrs={'class':'form-control', 'rows':3})
        }

class EmailForm(forms.ModelForm):
    class Meta:

        model = EmailNewsletter
        fields = ['email']
        widgets = {
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }
