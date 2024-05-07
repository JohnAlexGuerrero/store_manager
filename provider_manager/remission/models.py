from django.urls import reverse
from django.db import models
from django.db.models import Sum

from sales.models import OrderDetailSale

# Create your models here.
class Detail(models.Model):
    number = models.CharField(("numero"), max_length=10, null=False, unique=True)
    client = models.CharField(("señor"), max_length=100, null=False)
    orders = models.ManyToManyField(OrderDetailSale, verbose_name=("orders"))
    total = models.DecimalField(("total"), max_digits=10, decimal_places=2, default=0.0)
    created_at = models.DateField(("fecha"), auto_now=True)
    updated_at = models.DateField(("actualizacion"), auto_now=True)

    class Meta:
        verbose_name = ("Detail")
        verbose_name_plural = ("Details")

    def __str__(self):
        return self.client

    def get_absolute_url(self):
        return reverse("Detail_detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        items = OrderDetailSale.objects.filter(order=self.id)
        self.total = items.aggregate(Sum('total'))['total__sum']
        
        return super().save(*args, **kwargs)