# Generated by Django 4.0.1 on 2022-01-10 21:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_remove_booking_owner_pet_remove_pet_booking_pet_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='pet',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.pet'),
            preserve_default=False,
        ),
    ]
