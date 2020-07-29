# Generated by Django 3.0.8 on 2020-07-29 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kanatis_app', '0009_auto_20200729_1413'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='teamservices_ptr',
        ),
        migrations.AddField(
            model_name='team',
            name='id',
            field=models.AutoField(auto_created=True, default=True, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teamservices',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='kanatis_app.Team'),
        ),
    ]
