# Generated by Django 4.0.3 on 2022-03-09 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_remove_profile_verified_profile_is_email_verified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='verify_code',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
