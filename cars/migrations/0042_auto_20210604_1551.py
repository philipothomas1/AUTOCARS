# Generated by Django 3.1 on 2021-06-04 12:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0041_auto_20210604_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactinfomation',
            name='phone_number2',
            field=models.CharField(help_text='Phone Number', max_length=10, null=True, unique=True, validators=[django.core.validators.MinLengthValidator(10), django.core.validators.RegexValidator('0\\*\\d{9}', 'Your string should start with 0 and end with nine digits.')]),
        ),
    ]