# Generated by Django 5.0 on 2023-12-20 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0007_remove_bill_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='way_to_pay',
            field=models.CharField(choices=[(5, 'contado'), (15, 'credito 15 dias'), (30, 'credito 30 dias'), (40, 'credito 40 dias'), (60, 'credito 60 dias')], default=(5, 'contado'), max_length=100, verbose_name='forma de pago'),
        ),
    ]
