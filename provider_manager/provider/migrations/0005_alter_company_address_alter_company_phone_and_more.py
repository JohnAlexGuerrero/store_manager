# Generated by Django 5.0 on 2023-12-20 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0004_remove_order_product_order_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='direccion'),
        ),
        migrations.AlterField(
            model_name='company',
            name='phone',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='telefono'),
        ),
        migrations.AlterField(
            model_name='company',
            name='sellerman',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='vendedor'),
        ),
    ]