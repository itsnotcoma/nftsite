# Generated by Django 3.2.9 on 2021-12-09 19:08

from django.db import migrations, models
import marketplace.models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0017_auto_20211209_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='collection_image',
            field=models.ImageField(blank=True, max_length=256, null=True, upload_to=marketplace.models.Collection.collection_upload_img_url, verbose_name="Collection's image"),
        ),
        migrations.AlterField(
            model_name='nft',
            name='nft_image',
            field=models.ImageField(blank=True, max_length=256, null=True, upload_to=marketplace.models.NFT.nft_upload_img_url, verbose_name="NFT's image"),
        ),
    ]