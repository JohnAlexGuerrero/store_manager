# Generated by Django 5.0 on 2023-12-26 20:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0012_orderdetail_bill_delete_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderdetail',
            options={'ordering': ('-createdAt',), 'verbose_name': 'OrderDetail', 'verbose_name_plural': 'OrderDetails'},
        ),
    ]
