# Generated by Django 3.0.5 on 2020-05-02 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biz', '0006_biz_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hours',
            name='weekday',
            field=models.IntegerField(choices=[(1, 'Saturday'), (2, 'Sunday'), (3, 'Monday'), (4, 'Tuesday'), (5, 'Wednesday'), (6, 'Thursday'), (7, 'Friday')]),
        ),
    ]
