# Generated by Django 3.2.9 on 2021-11-03 01:33

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HotelRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('desc', models.CharField(max_length=500, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Номер отеля',
                'verbose_name_plural': 'Номера отеля',
            },
        ),
        migrations.CreateModel(
            name='RatingRooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('rating', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(0)], verbose_name='Оценка')),
                ('services', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='hotel.hotelroom', verbose_name='Оценка сервиса')),
            ],
            options={
                'verbose_name': 'Оценка сервиса номеров',
                'verbose_name_plural': 'Оценки сервиса номеров',
            },
        ),
        migrations.CreateModel(
            name='HotelFields',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('desc', models.CharField(max_length=500, verbose_name='Описание')),
                ('icon', models.CharField(max_length=500, verbose_name='Иконка')),
                ('about_room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='about_room', to='hotel.hotelroom', verbose_name='О номере')),
            ],
            options={
                'verbose_name': 'Поле номеров',
                'verbose_name_plural': 'Поля номеров',
            },
        ),
        migrations.CreateModel(
            name='BookingRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_date', models.CharField(max_length=50, verbose_name='Дата заезда')),
                ('depart_date', models.CharField(max_length=50, verbose_name='Дата выезда')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('comment', models.TextField(max_length=1000, verbose_name='Комментарий')),
                ('adult', models.PositiveIntegerField(default=1, verbose_name='Взрослые')),
                ('children', models.PositiveIntegerField(default=0, verbose_name='Дети')),
                ('rooms', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.hotelroom', verbose_name='Заказанный номер')),
            ],
            options={
                'verbose_name': 'Забронированный норме',
                'verbose_name_plural': 'Забронированные номера',
            },
        ),
    ]
