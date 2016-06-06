from django import forms
from django.conf import settings

from .models import Train
from .models import Invoice
#from .models import CustomUser


class TrainGetForm(forms.ModelForm):

    class Meta:
        model = Train
        fields = ['cityFrom', 'cityTo', 'date']

"""
class UserGetForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ['username', 'full_name', 'email', 'is_staff', 'password']
"""

class TrainCreateForm(forms.ModelForm):

    class Meta:
        model = Train
        fields = ['name', 'cost', 'cityFrom', 'cityTo', 'date']


class InvoiceCreateForm(forms.ModelForm):

    class Meta:
        model = Invoice
        fields = ['user', 'train', 'cost']
