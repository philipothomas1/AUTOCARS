# Generated by Django 3.1 on 2021-06-04 12:10

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0036_auto_20210604_1111'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfomation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number1', phone_field.models.PhoneField(help_text='Phone Number', max_length=100, null=True)),
                ('phone_number2', phone_field.models.PhoneField(help_text='Phone Number', max_length=10, null=True)),
                ('location', models.CharField(help_text='City name', max_length=15, null=True)),
                ('email', models.EmailField(max_length=30, null=True)),
                ('bank_account_number', models.CharField(max_length=30, null=True)),
            ],
            options={
                'verbose_name_plural': 'AutoParts',
            },
        ),
    ]
