# Generated by Django 3.2.9 on 2022-03-31 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0037_notifuserstatus'),
    ]

    operations = [
        migrations.CreateModel(
            name='notif_addnew',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isread', models.BooleanField()),
                ('ord', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='services.orders')),
            ],
        ),
    ]
