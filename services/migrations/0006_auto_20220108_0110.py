# Generated by Django 3.2.9 on 2022-01-07 23:10

from django.db import migrations, models
import services.models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='idnumber',
            new_name='id_number',
        ),
        migrations.AddField(
            model_name='person',
            name='avaregeincom',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=6),
        ),
        migrations.AddField(
            model_name='person',
            name='incometype',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='person',
            name='photo',
            field=models.FileField(null='True', upload_to=services.models.person.user_directory_path),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='person',
            name='sheltercondition',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='person',
            name='socialstatus',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='person',
            name='blod',
            field=models.CharField(default=None, max_length=90),
        ),
        migrations.AlterField(
            model_name='person',
            name='education',
            field=models.CharField(default=None, max_length=90),
        ),
        migrations.AlterField(
            model_name='person',
            name='familyumber',
            field=models.PositiveIntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='person',
            name='fathername',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.CharField(default=None, max_length=5),
        ),
        migrations.AlterField(
            model_name='person',
            name='helth',
            field=models.CharField(default=None, max_length=90),
        ),
    ]