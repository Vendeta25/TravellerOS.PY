from django.forms import ModelForm
from django import forms
from django.db import models
from .models import Ship
import datetime

class ShipRegisterForm(ModelForm):
    def __init__(self, *args, **kwargs):
         self.user = kwargs.pop('user',None)
         super(ShipRegisterForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        obj = super(ShipRegisterForm, self).save(commit=False)
        obj.created_date = datetime.datetime.now()
        obj.updated_date = datetime.datetime.now()       
        if commit:
            obj.save()           
        return obj
    class Meta:
        model = Ship
        fields = ['ship_name']


class CrewRegisterForm(forms.Form):
    ship_code = forms.CharField(max_length=100)

    