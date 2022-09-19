# Generated by Django 3.1 on 2021-05-27 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0014_auto_20210527_0924'),
    ]

    operations = [
        migrations.AddField(
            model_name='autoparts',
            name='category',
            field=models.CharField(blank=True, choices=[('BODY PARTS', 'BODY PARTS'), ('ENGINE & COMPONENTS', 'ENGINE & COMPONENTS'), ('CHASIS', 'CHASIS'), ('EXHAUST & COMPONENTS', 'EXHAUST & COMPONENTS'), ('EXTERIOR PARTS', 'EXTERIOR PARTS'), ('INTERIOR PARTS', 'INTERIOR PARTS'), ('LIGHTINGS', 'LIGHTINGS'), ('TIRES AND WHEELS', 'TIRES AND WHEELS'), ('SUSPENSION', 'SUSPENSION'), ('ELECTRONICS', 'ELECTRONICS'), ('OTHER PARTS', 'OTHER PARTS'), ('BRAKE SYSTEMS', 'BRAKE SYSTEMS')], max_length=20, null=True),
        ),
    ]