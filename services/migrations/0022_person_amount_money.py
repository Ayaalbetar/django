# Generated by Django 3.2.9 on 2022-03-18 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0021_alter_person_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='amount_money',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]
