# Generated by Django 3.2.9 on 2022-04-11 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0010_auto_20220411_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='map_location',
            name='lat',
            field=models.DecimalField(blank=True, decimal_places=3, default=0, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='map_location',
            name='lng',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=8),
        ),
    ]
