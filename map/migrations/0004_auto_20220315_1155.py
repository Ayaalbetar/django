# Generated by Django 3.2.9 on 2022-03-15 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0003_auto_20220315_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='map_location',
            name='lat',
            field=models.DecimalField(blank=True, decimal_places=20, default=0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='map_location',
            name='lng',
            field=models.DecimalField(blank=True, decimal_places=20, default=0, max_digits=20, null=True),
        ),
    ]
