# Generated by Django 3.2.12 on 2023-11-11 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoBack', '0004_remove_user_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_two_factor_enabled',
            field=models.BooleanField(default=False),
        ),
    ]