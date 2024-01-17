from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
set_unit_product = (
    ('und', 'unidad'),
    ('kl', 'kilo'),
    ('mts', 'metro'),
    ('m2', 'metro cuadrado'),
)

set_tax_product = (
    (1.19,'19 %'),
)

class Product(models.Model):
    description = models.CharField(("descripcion"), max_length=150, unique=True)
    code = models.CharField(("codigo"), max_length=50, unique=True)
    url = models.SlugField()
    stock = models.IntegerField(("disponible"), default=0)
    unit = models.CharField(("unidad"), max_length=50, choices=set_unit_product, default=set_unit_product[0])
    cost = models.DecimalField(("costo"), max_digits=10, decimal_places=2, default=0.0)
    tax = models.FloatField(("inpuesto"), default=0.0)
    cost_with_tax = models.DecimalField(("price"), max_digits=10, decimal_places=2, default=0.0)
    updatedAt = models.DateField(("actualizacion"), auto_now=False)

    class Meta:
        verbose_name = ("Product")
        verbose_name_plural = ("Products")

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse("Product_detail", kwargs={"slug": self.url})

    def save(self, *args, **kwargs):
        if not self.url:
            self.url = slugify(self.description)
        return super().save(*args, **kwargs)

class Category(models.Model):
    name = models.CharField(("description"), max_length=50, unique=True)
    slug = models.SlugField()
    products = models.ManyToManyField(Product, verbose_name=("products"))

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Category_detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        if self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)