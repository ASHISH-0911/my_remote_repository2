# Generated by Django 5.0.6 on 2024-07-12 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hydjobs',
            name='phonenumber',
            field=models.IntegerField(),
        ),
    ]
