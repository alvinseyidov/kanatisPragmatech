# Generated by Django 3.0.8 on 2020-08-05 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kanatis_app', '0013_auto_20200805_1402'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='gmap_embed_address_az',
            field=models.CharField(max_length=1000, null=True, verbose_name='Gmap embeded iframe'),
        ),
        migrations.AddField(
            model_name='contact',
            name='gmap_embed_address_en',
            field=models.CharField(max_length=1000, null=True, verbose_name='Gmap embeded iframe'),
        ),
        migrations.AddField(
            model_name='contact',
            name='gmap_embed_address_ru',
            field=models.CharField(max_length=1000, null=True, verbose_name='Gmap embeded iframe'),
        ),
    ]
