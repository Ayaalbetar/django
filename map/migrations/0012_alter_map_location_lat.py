# Generated by Django 3.2.9 on 2022-04-11 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0011_auto_20220411_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='map_location',
            name='lat',
            field=models.DecimalField(blank=True, decimal_places=6, default=0, max_digits=8, null=True),
        ),
    ]
