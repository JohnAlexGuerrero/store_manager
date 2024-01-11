# Generated by Django 5.0 on 2023-12-20 02:57

import django.db.models.deletion
import provider.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_product_cost_with_tax_alter_product_tax'),
        ('provider', '0002_bill_subtotal_bill_tax_company_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='items',
            field=models.IntegerField(default=0, verbose_name='items'),
        ),
        migrations.AlterField(
            model_name='bill',
            name='way_to_pay',
            field=models.CharField(choices=[(0, 'contado'), (15, 'credito 15 dias'), (30, 'credito 30 dias'), (40, 'credito 40 dias'), (60, 'credito 60 dias')], default=(0, 'contado'), max_length=100, verbose_name='forma de pago'),
        ),
        migrations.AlterField(
            model_name='order',
            name='bill',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='provider.bill', verbose_name='bill'),
        ),
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ManyToManyField(to='inventory.product', verbose_name='products'),
        ),
    ]
