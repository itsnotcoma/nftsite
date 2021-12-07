# Generated by Django 3.2.9 on 2021-12-06 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0014_rename_creator_nft_creators'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nft',
            name='creators',
        ),
        migrations.AddField(
            model_name='nft',
            name='creators',
            field=models.ManyToManyField(related_name='creators', to='marketplace.Creator'),
        ),
    ]