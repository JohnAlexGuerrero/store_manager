from django import forms
from sales.models import Order, Client, OrderDetailSale
from django.contrib.auth.models import User

def get_sellerman():
    return User.objects.first().username

def set_number_order():
    num_order = Order.objects.all().count()
    return f'{num_order + 4090}'

def get_bill_not_cancel():
    choices = (('Option 1', 'Option 1'),('Option 2', 'Option 2'),)
    order = Order.objects.filter(is_paid=False)[0]
    choices = ((order.id, order),)
    return choices
    
class OrderForm(forms.ModelForm):
    number = forms.CharField(initial=set_number_order)
    
    class Meta:
        model = Order
        fields = ("user","client","number","orderdetails","createdAt","total","coments")
        # exclude = ("user","client","createdAt","total","coments")

class ClientForm(forms.ModelForm):
    num_doc = forms.CharField(initial='22222222')
    address = forms.CharField(initial='no aplica')
    phone = forms.CharField(initial='000-000-0000')
    
    class Meta:
        model = Client
        fields = ("name","num_doc","address","phone")

class OrderDetailSaleForm(forms.ModelForm):
    # CHOICES = get_bill_not_cancel
    # order = forms.ChoiceField(choices=CHOICES, required=False)
    class Meta:
        model = OrderDetailSale
        fields = ("product","amount","price","dto")
