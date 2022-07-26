# Generated by Django 4.0.6 on 2022-07-30 04:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goats', '0002_goat_image'),
        ('cows', '0010_alter_cowinfo_options'),
        ('farmapp', '0006_schedule'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='schedule',
            options={'ordering': ['date']},
        ),
        migrations.CreateModel(
            name='Medical',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('reason', models.CharField(max_length=300)),
                ('date', models.DateField()),
                ('cow', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cows.cow')),
                ('goat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='goats.goat')),
            ],
        ),
    ]
