# Generated by Django 5.0.1 on 2024-01-27 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0007_order_subtotal_order_tax'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utility',
            name='createdAt',
            field=models.DateField(blank=True, null=True),
        ),
    ]
