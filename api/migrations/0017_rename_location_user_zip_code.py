# Generated by Django 4.0.1 on 2022-01-11 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_alter_booking_owner_of_pet'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='location',
            new_name='zip_code',
        ),
    ]