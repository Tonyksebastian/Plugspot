# Generated by Django 4.2.2 on 2023-09-17 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booknow',
            name='end_time',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='booknow',
            name='start_time',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='booknow',
            name='time',
            field=models.TimeField(null=True),
        ),
    ]