# Generated by Django 4.1.1 on 2022-10-24 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_property_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='price',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
