# Generated by Django 4.0.1 on 2022-01-11 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_user_location_user_zipcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(default='John Doe', max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='numReviews',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='rating',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
        ),
    ]