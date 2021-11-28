from django import forms
from .models import contact

class contactform(forms.ModelForm):
    class Meta:
        model= contact
        fields= ["name", "email", "phone", "desc"]

'''from django.forms.widgets import NumberInput, Widget

class contactform(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone = forms.IntegerField(required=True)
    desc = forms.CharField(
        required=True,
        widget=forms.Textarea
    )'''