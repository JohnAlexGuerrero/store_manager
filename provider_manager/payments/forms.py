from django import forms
from datetime import datetime

from django.contrib.auth.models import User
from payments.models import Provider
from provider.models import Bill

from django.db.models import Count

def set_reference():
    count = Provider.objects.all().count()
    return f'RCB - {count + 2931}'

def get_user():
    return User.objects.first()

# def get_bill_not_paid():
#     # bills = [x for x in Bill.objects.filter(is_paid=False)]
#     return bills

class ProviderForm(forms.ModelForm):
    reference = forms.CharField(initial=set_reference)
    # bill = forms.ChoiceField(choices=get_bill_not_paid, required=False)

    class Meta:
        model = Provider
        fields = ("user","reference","bill","value","description","createdAt")
        # widgets = {
        #     "bill": forms.Select(attrs={})
        # } 
    # def __init__(self,bill,*args, **kwargs):
    # #     # user = user
    #     bill = bill
    # #     # value = value
    # #     # description = description
    # #     # createdAt = createdAt
    #     super(ProviderForm, self).__init__(*args, **kwargs)
    # #     # self.fields['user'].initial = user
    #     self.fields['bill'].initial = bill
        # self.fields['value'].initial = value
        # self.fields['description'].initial = description
        # self.fields['createdAt'].initial = createdAt
