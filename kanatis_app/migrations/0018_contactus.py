# Generated by Django 3.0.8 on 2020-07-29 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kanatis_app', '0017_auto_20200729_1441'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=255)),
                ('desc', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Əlaqə Form',
            },
        ),
    ]
