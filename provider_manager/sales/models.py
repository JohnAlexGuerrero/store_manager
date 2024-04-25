from django.db import models
from django.urls import reverse
from inventory.models import Product
from django.contrib.auth.models import User
from decimal import Decimal
from django.db.models import Count, Sum

# Create your models here.
class Client(models.Model):
    name = models.CharField(("nombres"), max_length=150)
    num_doc = models.CharField(("cedula"), max_length=20, blank=True, null=True)
    address = models.CharField(("direccion"), max_length=50, blank=True, null=True)
    phone = models.CharField(("telefono"), max_length=50, blank=True, null=True)
    
    class Meta:
        verbose_name = ("Client")
        verbose_name_plural = ("Clients")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Client_detail", kwargs={"pk": self.pk})

class OrderDetailSale(models.Model):
    product = models.ForeignKey(Product, verbose_name=("products"), on_delete=models.CASCADE)
    amount = models.IntegerField(("cantidad"), default=0)
    price = models.DecimalField(("precio"), max_digits=10, decimal_places=2, default=0.0)
    dto = models.DecimalField(("descuento"), max_digits=10, decimal_places=2, default=0.0)
    total = models.DecimalField(("total"), max_digits=10, decimal_places=2, default=0.0)
    
    class Meta:
        verbose_name = ("OrderDetail")
        verbose_name_plural = ("OrderDetails")

    def __str__(self):
        return self.product.description

    def get_absolute_url(self):
        return reverse("OrderDetail_detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        self.total = (self.amount * self.price ) - self.dto    
        return super().save(*args, **kwargs)
    
class Order(models.Model):
    user = models.ForeignKey(User, verbose_name=("vendedor"), on_delete=models.CASCADE)
    client = models.ForeignKey(Client, verbose_name=("clients"), on_delete=models.CASCADE)
    number = models.CharField(("factura"), max_length=50, unique=True)
    orderdetails = models.ManyToManyField(OrderDetailSale, verbose_name=("orderdetailsales"))
    subtotal = models.DecimalField(("subtotal"), max_digits=10, decimal_places=2, default=0.0)
    tax = models.DecimalField(("impuesto"), max_digits=10, decimal_places=2, default=0.0)
    total = models.DecimalField(("total"), max_digits=10, decimal_places=2, default=0.0)
    coments = models.TextField(("observaciones"), blank=True, null=True)
    is_paid = models.BooleanField(("cancelado"), default=False)
    createdAt = models.DateField(("fecha"), auto_now=False)

    class Meta:
        verbose_name = ("Order")
        verbose_name_plural = ("Orders")
        ordering = ("-createdAt",)

    def __str__(self):
        return self.number

    def get_absolute_url(self):
        return reverse("Order_detail", kwargs={"pk": self.pk})
    
    def set_number_bill():
        return f'{4090 + Order.objects.all().count()}'

    def save(self, *args, **kwargs):
        items = OrderDetailSale.objects.filter(order=self.id)
        total = items.aggregate(Sum('total'))
        self.total = total['total__sum']
        self.subtotal = self.total / Decimal(1.19)
        self.tax = self.total - self.subtotal
        return super().save(*args, **kwargs)


class Utility(models.Model):
    orderdetail = models.ForeignKey(OrderDetailSale, verbose_name=("orderdetailsales"), on_delete=models.CASCADE)
    value = models.DecimalField(("valor"), max_digits=10, decimal_places=2, default=0.0)
    createdAt = models.DateField(auto_now_add=False, blank=True, null=True)
    
    class Meta:
        verbose_name = ("Utility")
        verbose_name_plural = ("Utilities")
        ordering = ("-createdAt",)

    def __str__(self):
        return f'{self.orderdetail}'

    def get_absolute_url(self):
        return reverse("Utility_detail", kwargs={"pk": self.pk})
