# Generated by Django 4.2.4 on 2024-01-23 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_service_station'),
    ]

    operations = [
        migrations.DeleteModel(
            name='service_station',
        ),
    ]