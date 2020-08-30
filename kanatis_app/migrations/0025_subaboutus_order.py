# Generated by Django 3.0.8 on 2020-08-28 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kanatis_app', '0024_auto_20200828_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='subaboutus',
            name='order',
            field=models.PositiveIntegerField(choices=[(1, 'First position'), (2, 'Second position'), (3, 'Third position'), (4, 'Fourth position'), (5, 'fifth position'), (6, 'sixth position'), (7, 'seventh position'), (8, 'eight position'), (9, 'ninenth position'), (10, 'tenth position')], default=1, verbose_name='Position ordering'),
        ),
    ]
