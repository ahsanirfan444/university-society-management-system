# Generated by Django 4.0.3 on 2022-03-09 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_profile_verify_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='verify_code',
            field=models.IntegerField(),
        ),
    ]
