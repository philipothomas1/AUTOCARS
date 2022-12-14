# Generated by Django 3.2.2 on 2021-05-09 21:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_name', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Drive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drivetrain', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FuelType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fuel_type', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Make',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make_name', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Trannsmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transmision', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(blank=True, help_text='Harrier 240G', max_length=20, null=True)),
                ('price', models.IntegerField(blank=True, default='0', null=True)),
                ('mileage', models.IntegerField(blank=True, default='0', null=True)),
                ('engine', models.CharField(blank=True, help_text='Engine cc', max_length=20, null=True)),
                ('color', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='cars.color')),
                ('drive', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='cars.drive')),
                ('fueltype', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='cars.fueltype')),
                ('make', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='cars.make')),
                ('transmission', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='cars.trannsmission')),
            ],
        ),
    ]
