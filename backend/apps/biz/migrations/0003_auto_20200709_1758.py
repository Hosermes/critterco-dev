# Generated by Django 3.0.7 on 2020-07-09 13:28

import django.contrib.gis.db.models.fields
import django.core.validators
from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('biz', '0002_auto_20200604_2313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biz',
            name='gallery',
            field=models.ImageField(blank=True, default='', upload_to=''),
        ),
        migrations.AlterField(
            model_name='biz',
            name='instagram',
            field=models.CharField(blank=True, default='', max_length=255, validators=[django.core.validators.RegexValidator(message='Please enter a valid Instagram ID.', regex='^(?:(?:http|https):\\/\\/)?(?:www\\.)?(?:instagram\\.com|instagr\\.am)\\/([A-Za-z0-9-_\\.]+)')]),
        ),
        migrations.AlterField(
            model_name='biz',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326),
        ),
        migrations.AlterField(
            model_name='biz',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None),
        ),
        migrations.AlterField(
            model_name='biz',
            name='phone2',
            field=models.CharField(blank=True, default='', max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the following format: '02112345678'.", regex='^0\\d{2}\\d{8}$')]),
        ),
        migrations.AlterField(
            model_name='biz',
            name='telegram',
            field=models.CharField(blank=True, default='', max_length=255, validators=[django.core.validators.RegexValidator(message='Please enter a valid Telegram ID.', regex='^(?:(?:http|https):\\/\\/)?(?:www\\.)?(?:telegram\\.me|t\\.me|telegram.dog)\\/([A-Za-z0-9-_\\.]+)$')]),
        ),
        migrations.AlterField(
            model_name='biz',
            name='website',
            field=models.URLField(blank=True, default='', max_length=50),
        ),
    ]
