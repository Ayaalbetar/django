# Generated by Django 3.2.9 on 2022-03-09 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0018_alter_person_id_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='address',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.CharField(blank=True, default=None, max_length=5, null=True),
        ),
    ]
