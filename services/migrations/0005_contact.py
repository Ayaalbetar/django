# Generated by Django 3.2.9 on 2021-11-21 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_auto_20211121_1348'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('tele', models.IntegerField(default=0)),
                ('phone', models.IntegerField(default=0)),
                ('job', models.CharField(max_length=100)),
                ('placejob', models.CharField(max_length=100)),
                ('job2', models.CharField(blank=True, max_length=100)),
                ('personcontact', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='services.person')),
            ],
        ),
    ]
