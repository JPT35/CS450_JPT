# Generated by Django 4.1.7 on 2023-04-22 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0007_remove_client_industry'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='address',
            field=models.CharField(default='unknown', max_length=255),
        ),
    ]
