# Generated by Django 4.0.3 on 2022-03-09 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_profile_two_step_verify_code_profile_twostep'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='two_step_verify_code',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='twostep',
        ),
        migrations.AddField(
            model_name='profile',
            name='failed_attempt',
            field=models.IntegerField(default=0),
        ),
    ]
