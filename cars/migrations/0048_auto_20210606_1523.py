# Generated by Django 3.1 on 2021-06-06 12:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0047_auto_20210606_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactinfomation',
            name='location',
            field=models.CharField(help_text='City name', max_length=15, null=True, validators=[django.core.validators.RegexValidator('^[-a-zA-Z]', 'Contain letters only')]),
        ),
    ]
