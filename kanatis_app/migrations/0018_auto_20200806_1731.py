# Generated by Django 3.0.8 on 2020-08-06 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kanatis_app', '0017_auto_20200806_1713'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='ofice_phone',
            new_name='office_phone',
        ),
    ]