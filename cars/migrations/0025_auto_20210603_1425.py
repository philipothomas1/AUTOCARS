# Generated by Django 3.1 on 2021-06-03 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0024_auto_20210603_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cars.color'),
        ),
    ]
