# Generated by Django 3.2.9 on 2022-03-22 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0008_alter_map_location_lat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='map_location',
            name='lat',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=6, null=True),
        ),
    ]