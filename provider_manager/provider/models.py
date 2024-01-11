from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.db.models import Count

from inventory.models import Product, set_tax_product

# Create your models here.
set_way_to_pay = (
    (1,'contado'),(2,'credito')
)

class Company(models.Model):
    name = models.CharField(("empresa"), max_length=150, unique=True)
    url = models.SlugField()
    address = models.CharField(("direccion"), max_length=100, null=True, blank=True)
    phone = models.CharField(("telefono"), max_length=50, null=True, blank=True)
    sellerman = models.CharField(("vendedor"), max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = ("Company")
        verbose_name_plural = ("Companies")

    def __str__(self):
        return self.name.upper()

    def get_absolute_url(self):
        return reverse("Company_detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        if not self.url:
            self.url = slugify(self.name)
        return super().save(*args, **kwargs)

class Bill(models.Model):
    company = models.ForeignKey(Company, verbose_name=("companies"), on_delete=models.CASCADE)
    number = models.CharField(("factura"), max_length=50, unique=True)
    createdAt = models.DateField(("facturacion"), auto_now=False)
    expirationAt = models.DateField(("vencimiento"), auto_now=False)
    is_credit = models.BooleanField(("credito"))
    way_to_pay = models.IntegerField(("forma de pago"), choices=set_way_to_pay, default=set_way_to_pay[0])
    subtotal = models.DecimalField(("subtotal"), max_digits=10, decimal_places=2, default=0.0)
    tax = models.DecimalField(("impuesto"), max_digits=10, decimal_places=2, default=0.0)
    total = models.DecimalField(("total"), max_digits=10, decimal_places=2, default=0.0)

    class Meta:
        verbose_name = ("Bill")
        verbose_name_plural = ("Bills")
        ordering = ["-createdAt"]

    def __str__(self):
        return self.number

    def get_absolute_url(self):
        return reverse("Bill_detail", kwargs={"pk": self.pk})
    
    def count_items(self):
        return ''#Order.objects.filter(order__bill=self.id).count()


        

class OrderDetail(models.Model):
    bill = models.ForeignKey(Bill, verbose_name=("bill"), on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name=("product"), on_delete=models.CASCADE)
    quantity = models.IntegerField(("cantidad"), default=0)
    price = models.DecimalField(("precio"), max_digits=10, decimal_places=2, default=0.0)
    tax = models.FloatField(("iva"), default=0.0, choices=set_tax_product)
    total = models.DecimalField(("total"), max_digits=10, decimal_places=2, default=0.0)
    createdAt = models.DateField(("creado"), auto_now=False)
    

    class Meta:
        verbose_name = ("OrderDetail")
        verbose_name_plural = ("OrderDetails")
        ordering = ("-createdAt",)

    def __str__(self):
        return f'{self.product}'

    def get_absolute_url(self):
        return reverse("OrderDetail_detail", kwargs={"pk": self.pk})
    
    def save(self, *args, **kwargs):
        if self.total == 0.0:  
            self.total = (self.quantity * self.price)
        return super().save(*args, **kwargs)

