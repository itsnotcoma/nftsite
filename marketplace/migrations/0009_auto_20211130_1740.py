# Generated by Django 3.2.9 on 2021-11-30 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0008_alter_collection_nfts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='nfts',
            field=models.ManyToManyField(related_name='nfts', to='marketplace.NFT', verbose_name='NFT'),
        ),
        migrations.AlterField(
            model_name='nft',
            name='nft_name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Token Name'),
        ),
    ]
