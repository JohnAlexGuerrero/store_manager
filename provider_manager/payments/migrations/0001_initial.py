# Generated by Django 5.0 on 2023-12-21 15:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('provider', '0010_alter_bill_way_to_pay_alter_order_tax'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='valor')),
                ('description', models.CharField(blank=True, max_length=50, null=True, verbose_name='descripcion')),
                ('createdAt', models.DateField(verbose_name='fecha')),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='provider.bill', verbose_name='bills')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'Provider',
                'verbose_name_plural': 'Providers',
            },
        ),
    ]