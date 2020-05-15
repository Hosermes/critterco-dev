# Generated by Django 3.0.5 on 2020-05-10 11:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biz', '0009_biz_phone2'),
    ]

    operations = [
        migrations.AddField(
            model_name='biz',
            name='instagram',
            field=models.CharField(blank=True, max_length=255, null=True, validators=[django.core.validators.RegexValidator(message='Please enter a valid Instagram ID.', regex='^(?:(?:http|https):\\/\\/)?(?:www\\.)?(?:instagram\\.com|instagr\\.am)\\/([A-Za-z0-9-_\\.]+)')]),
        ),
        migrations.AddField(
            model_name='biz',
            name='website',
            field=models.URLField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='biz',
            name='phone2',
            field=models.CharField(blank=True, max_length=11, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the following format: '02112345678'.", regex='^0\\d{2}\\d{8}$')]),
        ),
    ]