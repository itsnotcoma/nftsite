# Generated by Django 3.2.9 on 2021-12-10 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0028_auto_20211210_2056'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='collection',
            options={'ordering': ['-created', '-updated'], 'verbose_name': 'Collection', 'verbose_name_plural': 'Collections'},
        ),
        migrations.AlterModelOptions(
            name='creator',
            options={'verbose_name': 'Creator'},
        ),
        migrations.AddField(
            model_name='collection',
            name='creator_c',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='creator_c', to='marketplace.creator'),
        ),
    ]