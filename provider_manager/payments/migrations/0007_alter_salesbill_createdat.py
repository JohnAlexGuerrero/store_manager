# Generated by Django 5.0.1 on 2024-01-27 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0006_provider_reference'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesbill',
            name='createdAt',
            field=models.DateField(verbose_name='creado'),
        ),
    ]
