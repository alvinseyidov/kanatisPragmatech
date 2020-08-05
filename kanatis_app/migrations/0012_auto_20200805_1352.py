# Generated by Django 3.0.8 on 2020-08-05 13:52

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kanatis_app', '0011_auto_20200805_1335'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='description_az',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='description_en',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='description_ru',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='title_az',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='title_en',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='title_ru',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='carousel',
            name='content_az',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='carousel',
            name='content_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='carousel',
            name='content_ru',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='description_az',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='description_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='description_ru',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='name_az',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='name_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='name_ru',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='subservice',
            name='content_az',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='subservice',
            name='content_en',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='subservice',
            name='content_ru',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='subservice',
            name='title_az',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='subservice',
            name='title_en',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='subservice',
            name='title_ru',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='desc_az',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='desc_en',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='desc_ru',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='name_az',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='name_en',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='name_ru',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='status_az',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='status_en',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='status_ru',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='textpages',
            name='team_az',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='textpages',
            name='team_en',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='textpages',
            name='team_member_az',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='textpages',
            name='team_member_en',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='textpages',
            name='team_member_ru',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='textpages',
            name='team_ru',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
