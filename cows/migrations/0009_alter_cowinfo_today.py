# Generated by Django 4.0.6 on 2022-07-29 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cows', '0008_cowinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cowinfo',
            name='today',
            field=models.DateField(),
        ),
    ]
