# Generated by Django 5.1.7 on 2025-04-05 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('br', '0004_estado_main_activities_estado_tourist_attractions_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estado',
            name='gdp',
            field=models.CharField(max_length=1000),
        ),
    ]
