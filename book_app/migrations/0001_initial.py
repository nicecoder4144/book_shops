# Generated by Django 5.0.2 on 2024-02-07 12:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=40, verbose_name='Muallifi')),
                ('status', models.BooleanField(default=True, verbose_name='Holati')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Muallif',
                'verbose_name_plural': 'Mualliflar',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Categoriya nomi')),
                ('status', models.BooleanField(default=True, verbose_name='Holati')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Kategoriya',
                'verbose_name_plural': 'Kategoriyalar',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField(verbose_name="ta'rif")),
                ('photo', models.ImageField(upload_to='book_photo/%Y/%m/%d/', verbose_name='Rasmi')),
                ('isbn', models.PositiveIntegerField(verbose_name='Kitobning id raqami')),
                ('file', models.FileField(upload_to='book_file/%Y/%m/%d/', verbose_name='File')),
                ('audio', models.FileField(upload_to='book_audio/%Y/%m/%d/', verbose_name='Audiosi')),
                ('dounloads_count', models.PositiveIntegerField(default=0, verbose_name='Yuklab olishlar soni')),
                ('status', models.BooleanField(default=True, verbose_name='Holati')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_app.author', verbose_name='Muallifi')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_app.category', verbose_name='Kategoriyasi')),
            ],
            options={
                'verbose_name': 'Kitob',
                'verbose_name_plural': 'Kitoblar',
            },
        ),
    ]
