# Generated by Django 4.0.3 on 2022-03-09 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_remove_profile_is_email_verfified_profile_verified'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='verified',
        ),
        migrations.AddField(
            model_name='profile',
            name='is_email_verified',
            field=models.BooleanField(default=False),
        ),
    ]
