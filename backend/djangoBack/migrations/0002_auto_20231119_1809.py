# Generated by Django 3.2.12 on 2023-11-19 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoBack', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='game_socket_id',
            field=models.CharField(blank=True, default='NONE', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='socket_id',
            field=models.CharField(blank=True, default='NONE', max_length=255, null=True),
        ),
    ]
