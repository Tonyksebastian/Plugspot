# Generated by Django 4.2.4 on 2024-02-21 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('make_service', '0003_remove_service_booking_service_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='service_booking',
            name='time',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='service_booking',
            name='date',
            field=models.DateField(null=True),
        ),
    ]