# Generated by Django 5.0.1 on 2024-01-20 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0006_remove_orderdetailsale_order_order_orderdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='subtotal',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='subtotal'),
        ),
        migrations.AddField(
            model_name='order',
            name='tax',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='impuesto'),
        ),
    ]