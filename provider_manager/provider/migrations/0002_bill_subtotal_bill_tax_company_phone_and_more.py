# Generated by Django 5.0 on 2023-12-19 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='subtotal',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='subtotal'),
        ),
        migrations.AddField(
            model_name='bill',
            name='tax',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='impuesto'),
        ),
        migrations.AddField(
            model_name='company',
            name='phone',
            field=models.CharField(max_length=50, null=True, verbose_name='telefono'),
        ),
        migrations.AddField(
            model_name='company',
            name='sellerman',
            field=models.CharField(max_length=50, null=True, verbose_name='vendedor'),
        ),
        migrations.AlterField(
            model_name='company',
            name='address',
            field=models.CharField(max_length=100, null=True, verbose_name='direccion'),
        ),
    ]
