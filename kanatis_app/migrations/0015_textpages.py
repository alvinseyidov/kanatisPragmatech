# Generated by Django 3.0.8 on 2020-07-29 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kanatis_app', '0014_auto_20200729_1425'),
    ]

    operations = [
        migrations.CreateModel(
            name='TextPages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_member', models.CharField(blank=True, max_length=255, null=True)),
                ('team', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
