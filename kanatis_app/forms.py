from django import forms
from .models import *


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'subject', 'desc']
        widgets = {
            'name': forms.TextInput(attrs={
                'name': "name",
                'type': "text",
                'class': "form-control",
                'placeholder': "Name"
            }),
            'subject': forms.TextInput(attrs={
                'name': "surname",
                'type': "text",
                'class': "form-control",
                'placeholder': "Subject"
            }),
            'email': forms.TextInput(attrs={
                'name': "email",
                'type': "email",
                'class': "form-control",
                'placeholder': "Email"
            }),
            'desc': forms.Textarea(attrs={
                'name': "text",
                'type': "text",
                'rows': 4,
                'class': "form-control",
                'placeholder': "Message"
            })
        }
