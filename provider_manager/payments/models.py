from django.db import models
from django.urls import reverse
from decimal import Decimal

from django.contrib.auth.models import User
from django.db.models import Sum

from sales.models import Order, Utility
from provider.models import Bill
from sales.models import OrderDetailSale

# Create your models here.
set_way_to_pay = (
    ('e','efectivo'),
    ('n','nequi'),
    ('b','bancolombia'),
    ('bb','banco bogota'),
    ('bcs','caja social'),
    ('bd','davivienda'),
)

class Provider(models.Model):
    reference = models.CharField(("referencia"), max_length=50, unique=True)
    user = models.ForeignKey(User, verbose_name=("user"), on_delete=models.CASCADE)
    bill = models.ForeignKey(Bill, verbose_name=("bills"), on_delete=models.CASCADE)
    value = models.DecimalField(("valor"), max_digits=10, decimal_places=2, default=0.0)
    description = models.TextField(("descripcion"), max_length=50, null=True, blank=True)
    createdAt = models.DateField(("fecha"), auto_now=False)

    class Meta:
        verbose_name = ("Provider")
        verbose_name_plural = ("Providers")
        ordering = ("-createdAt",)

    def __str__(self):
        return self.bill.number

    def get_absolute_url(self):
        return reverse("Provider_detail", kwargs={"pk": self.pk})
    
    def save(self, *args, **kwargs):
        is_paid = False
        bill = Bill.objects.get(id=self.bill.id)

        if (bill.total - self.value) == 0:
            is_paid = True
        else:
            res_value = bill.total - (self.total_pays() + self.value)

            if res_value <= 100:
                is_paid = True
        
        if is_paid:
            bill.is_paid = is_paid
            bill.save()
        return super().save(*args, **kwargs)
    
    def total_balance(self):
        total = 0
        payments = Provider.objects.filter(bill=self.bill.id)
        if payments:
            total = payments.aggregate(Sum('value'))['value__sum']
        return total
    
    def total_pays(self):
        total = 0
        query = Provider.objects.filter(bill=self.bill.id).aggregate(Sum('value'))
        if query["value__sum"] != None:
          total = query["value__sum"]
        return total

class SalesBill(models.Model):
    order = models.ForeignKey(Order, verbose_name=("orders"), on_delete=models.CASCADE)
    total = models.DecimalField(("value"), max_digits=10, decimal_places=2, default=0.0)
    way_to_pay = models.CharField(("tipo pago"), max_length=10, choices=set_way_to_pay, default=set_way_to_pay[0])
    createdAt = models.DateField(("creado"), auto_now_add=False)

    class Meta:
        verbose_name = ("SalesBill")
        verbose_name_plural = ("SalesBills")
        ordering = ("-createdAt",)

    def __str__(self):
        return self.order.number

    def get_absolute_url(self):
        return reverse("Bill_detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        order_details = OrderDetailSale.objects.filter(order_id=self.order.id)
        print(order_details)
        
        for item in order_details:
            value_ = item.total - (item.product.cost_with_tax * item.amount)
            util = Utility(orderdetail_id=item.id, value=value_, createdAt=self.order.createdAt)
            util.save()
        
        return super().save(*args, **kwargs)