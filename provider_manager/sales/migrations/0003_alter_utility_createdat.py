# Generated by Django 5.0 on 2024-01-03 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_alter_order_options_utility'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utility',
            name='createdAt',
            field=models.DateField(auto_now_add=True),
        ),
    ]
