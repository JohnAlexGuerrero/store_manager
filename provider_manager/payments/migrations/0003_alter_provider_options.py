# Generated by Django 5.0 on 2023-12-26 20:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_alter_provider_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='provider',
            options={'ordering': ('-createdAt',), 'verbose_name': 'Provider', 'verbose_name_plural': 'Providers'},
        ),
    ]
