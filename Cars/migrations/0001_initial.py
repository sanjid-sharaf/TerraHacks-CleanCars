# Generated by Django 5.0.7 on 2024-08-04 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('year', models.PositiveIntegerField()),
                ('fueltype', models.CharField(max_length=50)),
                ('drive', models.CharField(max_length=50)),
                ('displ', models.FloatField()),
                ('city08', models.FloatField()),
                ('highway08', models.FloatField()),
                ('co2', models.FloatField()),
                ('fuelcost08', models.FloatField()),
                ('trany', models.CharField(max_length=50)),
                ('vclass', models.CharField(max_length=50)),
            ],
        ),
    ]