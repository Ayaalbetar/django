# Generated by Django 3.2.9 on 2022-03-23 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0024_auto_20220322_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='contact',
            field=models.ManyToManyField(through='services.orders', to='services.person'),
        ),
    ]