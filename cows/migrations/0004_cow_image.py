# Generated by Django 4.0.6 on 2022-07-25 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cows', '0003_alter_cow_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='cow',
            name='image',
            field=models.ImageField(default='cowdefault.jpg', upload_to='cowImages/'),
        ),
    ]
