# Generated by Django 3.2.9 on 2021-12-06 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0010_auto_20211130_1755'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nft',
            name='creator',
        ),
        migrations.AddField(
            model_name='nft',
            name='creators',
            field=models.ManyToManyField(null=True, related_name='creators', to='marketplace.Creator'),
        ),
    ]
