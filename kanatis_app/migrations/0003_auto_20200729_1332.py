# Generated by Django 3.0.8 on 2020-07-29 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kanatis_app', '0002_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='img',
            field=models.ImageField(upload_to='teams'),
        ),
    ]
