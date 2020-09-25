# Generated by Django 3.0.8 on 2020-09-25 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kanatis_app', '0033_auto_20200830_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='desc_az',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='contactus',
            name='desc_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='contactus',
            name='email_az',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='contactus',
            name='email_en',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='contactus',
            name='name_az',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='contactus',
            name='name_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='contactus',
            name='subject_az',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='contactus',
            name='subject_en',
            field=models.CharField(max_length=255, null=True),
        ),
    ]