# Generated by Django 5.0 on 2024-01-03 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0003_alter_utility_createdat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utility',
            name='createdAt',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]