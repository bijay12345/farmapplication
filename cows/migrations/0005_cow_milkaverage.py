# Generated by Django 4.0.6 on 2022-07-25 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cows', '0004_cow_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='cow',
            name='milkAverage',
            field=models.FloatField(default=1),
        ),
    ]