# Generated by Django 4.0.3 on 2022-03-08 07:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('console', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classroom',
            name='club',
        ),
        migrations.AddField(
            model_name='classroom',
            name='book_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='boot_to', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Booking',
        ),
    ]
