# Generated by Django 3.2.9 on 2022-03-24 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0028_family_c'),
    ]

    operations = [
        migrations.AlterField(
            model_name='family',
            name='elderliness',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='family',
            name='num_fmale',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='family',
            name='num_male',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='family',
            name='trestles',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
