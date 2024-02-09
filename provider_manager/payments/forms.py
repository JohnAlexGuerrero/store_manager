from django import forms
from datetime import datetime

from django.contrib.auth.models import User
from payments.models import Provider
from provider.models import Bill

from django.db.models import Count


class ProviderForm(forms.ModelForm):
    reference = forms.CharField()
    user = forms.Select()
    bill = forms.Select()
    value = forms.CharField()
    description = forms.Textarea()
    createdAt = forms.DateField()

    class Meta:
        model = Provider
        fields = ("user","reference","bill","value","description","createdAt")
        