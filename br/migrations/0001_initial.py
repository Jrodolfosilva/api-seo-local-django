# Generated by Django 5.1.7 on 2025-04-01 18:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('name', models.CharField(max_length=100)),
                ('full_name', models.CharField(max_length=255)),
                ('population', models.IntegerField()),
                ('area_km2', models.FloatField()),
                ('population_density', models.FloatField()),
                ('demonym', models.CharField(max_length=50)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('ibge_code', models.IntegerField()),
                ('main_zip_code', models.CharField(max_length=10)),
                ('zip_code_range', models.CharField(max_length=20)),
                ('seo_title', models.CharField(max_length=160)),
                ('meta_description', models.TextField()),
                ('appropriate_preposition', models.CharField(max_length=2)),
                ('description_text', models.TextField()),
                ('map_embed', models.URLField()),
                ('gdp', models.BigIntegerField()),
                ('hdi', models.FloatField()),
                ('climate', models.CharField(max_length=50)),
                ('history', models.TextField()),
                ('main_activities', models.JSONField()),
                ('tourist_attractions', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('name', models.CharField(max_length=100)),
                ('full_name', models.CharField(max_length=255)),
                ('population', models.IntegerField()),
                ('area_km2', models.FloatField()),
                ('population_density', models.FloatField()),
                ('demonym', models.CharField(max_length=50)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('ibge_code', models.IntegerField()),
                ('main_zip_code', models.CharField(max_length=10)),
                ('zip_code_range', models.CharField(max_length=20)),
                ('seo_title', models.CharField(max_length=160)),
                ('meta_description', models.TextField()),
                ('appropriate_preposition', models.CharField(max_length=2)),
                ('description_text', models.TextField()),
                ('map_embed', models.URLField()),
                ('gdp', models.BigIntegerField()),
                ('hdi', models.FloatField()),
                ('climate', models.CharField(max_length=50)),
                ('history', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Bairro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('name', models.CharField(max_length=100)),
                ('full_name', models.CharField(max_length=255)),
                ('population', models.IntegerField()),
                ('area_km2', models.FloatField()),
                ('population_density', models.FloatField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('zip_code', models.CharField(max_length=10)),
                ('seo_title', models.CharField(max_length=160)),
                ('meta_description', models.TextField()),
                ('appropriate_preposition', models.CharField(max_length=2)),
                ('description_text', models.TextField()),
                ('map_embed', models.URLField()),
                ('gdp', models.BigIntegerField()),
                ('hdi', models.FloatField()),
                ('climate', models.CharField(max_length=50)),
                ('history', models.TextField()),
                ('main_activities', models.JSONField()),
                ('points_of_interest', models.JSONField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='br.cidade')),
            ],
        ),
        migrations.AddField(
            model_name='cidade',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='br.estado'),
        ),
    ]
