# Generated by Django 4.2.4 on 2024-02-21 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('make_service', '0004_service_booking_time_alter_service_booking_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='service_booking',
            name='vehno',
            field=models.CharField(default='', max_length=250),
        ),
    ]