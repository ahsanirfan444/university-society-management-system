# Generated by Django 4.0.3 on 2022-03-09 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_profile_is_email_verfified_profile_verify_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='verify_code',
            field=models.IntegerField(max_length=5),
        ),
    ]
