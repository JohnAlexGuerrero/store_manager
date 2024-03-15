from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.db.models import Count, Sum
from decimal import Decimal

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
        ordering = ('name',)

    def __str__(self):
        return self.name.upper()

    def get_absolute_url(self):
        return reverse("Company_detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        if not self.url:
            self.url = slugify(self.name)
        return super().save(*args, **kwargs)
    
    def balance(self):
        result_balance = 0
        bills = self.bills_is_pending()
        if bills != None:
            result = [x.total for x in bills]
            result_balance = sum(result)

        return result_balance
    
    def bills_is_pending(self):
        query = Bill.objects.filter(is_paid=0, company_id=self.id).order_by('company__name')
        if query:
            return query
        return None
    
class OrderDetail(models.Model):
    product = models.ForeignKey(Product, verbose_name=("product"), on_delete=models.CASCADE)
    quantity = models.IntegerField(("cantidad"), default=0)
    price = models.DecimalField(("precio"), max_digits=10, decimal_places=2, default=0.0)
    tax = models.FloatField(("iva"), default=set_tax_product[0], choices=set_tax_product)
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
        self.total = (self.quantity * self.price)
        return super().save(*args, **kwargs)

class Bill(models.Model):
    company = models.ForeignKey(Company, verbose_name=("companies"), on_delete=models.CASCADE)
    number = models.CharField(("factura"), max_length=50, unique=True)
    way_to_pay = models.IntegerField(("forma de pago"), choices=set_way_to_pay, default=set_way_to_pay[0])
    subtotal = models.DecimalField(("subtotal"), max_digits=10, decimal_places=2, default=0.0)
    tax = models.DecimalField(("impuesto"), max_digits=10, decimal_places=2, default=0.0)
    total = models.DecimalField(("total"), max_digits=10, decimal_places=2, default=0.0)
    is_credit = models.BooleanField(("credito"))
    is_paid = models.BooleanField(("cancelado"), default=False)
    order = models.ManyToManyField(OrderDetail, verbose_name=("order"))
    createdAt = models.DateField(("facturacion"), auto_now=False)
    expirationAt = models.DateField(("vencimiento"), auto_now=False)

    class Meta:
        verbose_name = ("Bill")
        verbose_name_plural = ("Bills")
        ordering = ["-createdAt"]

    def __str__(self):
        return self.number

    def get_absolute_url(self):
        return reverse("Bill_detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        query = OrderDetail.objects.filter(bill=self.id, bill__createdAt=self.createdAt)
        print(query.values())
        total = query.aggregate(Sum('total'))
        if total["total__sum"] != None:
            self.subtotal = total["total__sum"]
            self.total = total['total__sum'] * Decimal(1.19)
            self.tax = self.total - self.subtotal

        
        return super().save(*args, **kwargs)




        




