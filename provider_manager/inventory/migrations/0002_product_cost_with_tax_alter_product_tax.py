# Generated by Django 5.0 on 2023-12-19 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cost_with_tax',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='price'),
        ),
        migrations.AlterField(
            model_name='product',
            name='tax',
            field=models.FloatField(default=0.0, verbose_name='inpuesto'),
        ),
    ]
