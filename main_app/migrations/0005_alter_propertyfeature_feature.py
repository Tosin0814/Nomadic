# Generated by Django 4.1.1 on 2022-10-26 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_property_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertyfeature',
            name='feature',
            field=models.CharField(max_length=30),
        ),
    ]
