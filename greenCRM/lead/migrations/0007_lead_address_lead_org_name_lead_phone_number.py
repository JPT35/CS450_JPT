# Generated by Django 4.1.7 on 2023-04-22 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0006_leadfile'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='address',
            field=models.CharField(default='unknown', max_length=255),
        ),
        migrations.AddField(
            model_name='lead',
            name='org_name',
            field=models.CharField(default='unknown', max_length=225),
        ),
        migrations.AddField(
            model_name='lead',
            name='phone_number',
            field=models.CharField(default='unknown', max_length=20),
        ),
    ]
