# Generated by Django 3.2.9 on 2022-01-07 23:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_auto_20220108_0110'),
    ]

    operations = [
        migrations.CreateModel(
            name='content_serv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_serv', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=40)),
                ('phone', models.PositiveIntegerField()),
                ('contact', models.ManyToManyField(through='services.content_serv', to='services.services')),
            ],
        ),
        migrations.CreateModel(
            name='orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_order', models.CharField(max_length=20)),
                ('date_order', models.DateTimeField(auto_now_add=True)),
                ('idperson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='services.person')),
                ('idserv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='services.services')),
            ],
        ),
        migrations.AddField(
            model_name='content_serv',
            name='idposition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='services.position'),
        ),
        migrations.AddField(
            model_name='content_serv',
            name='idserv',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='content', to='services.services'),
        ),
    ]
