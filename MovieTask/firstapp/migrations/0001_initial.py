# Generated by Django 4.2.7 on 2024-03-21 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=240, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('actors', models.TextField()),
                ('img', models.ImageField(upload_to='gallery')),
                ('desc', models.TextField()),
                ('date', models.DateField()),
                ('url', models.URLField(max_length=120)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.topic')),
            ],
        ),
    ]
