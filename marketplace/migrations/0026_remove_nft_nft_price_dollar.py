# Generated by Django 3.2.9 on 2021-12-10 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0025_auto_20211210_1340'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nft',
            name='nft_price_dollar',
        ),
    ]
