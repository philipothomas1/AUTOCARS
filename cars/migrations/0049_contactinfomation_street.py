# Generated by Django 3.1 on 2021-06-06 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0048_auto_20210606_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactinfomation',
            name='street',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
