# Generated by Django 3.1 on 2021-06-02 18:15

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0020_auto_20210602_2031'),
    ]

    operations = [
        migrations.AddField(
            model_name='cars',
            name='added_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='cars',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='added_on'),
        ),
    ]