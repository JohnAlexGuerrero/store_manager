# Generated by Django 5.0 on 2023-12-30 16:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0005_category'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='nombres')),
                ('num_doc', models.CharField(blank=True, max_length=20, null=True, verbose_name='cedula')),
                ('address', models.CharField(blank=True, max_length=50, null=True, verbose_name='direccion')),
                ('phone', models.CharField(blank=True, max_length=50, null=True, verbose_name='telefono')),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=50, unique=True, verbose_name='factura')),
                ('createdAt', models.DateField(verbose_name='fecha')),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='total')),
                ('coments', models.TextField(blank=True, null=True, verbose_name='observaciones')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.client', verbose_name='clients')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='vendedor')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='OrderDetailSale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0, verbose_name='cantidad')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='precio')),
                ('dto', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='descuento')),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='total')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.order', verbose_name='orders')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.product', verbose_name='products')),
            ],
            options={
                'verbose_name': 'OrderDetail',
                'verbose_name_plural': 'OrderDetails',
            },
        ),
    ]