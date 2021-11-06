from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.

class HotelRoom(models.Model):
    title = models.CharField("Название", max_length=50)
    desc = models.CharField("Описание", max_length=500)
    image = models.ImageField("Фото", upload_to="room/", null=True, blank=True)

    class Meta:
        verbose_name = "Номер отеля"
        verbose_name_plural = "Номера отеля"

    def __str__(self):
        return self.title

class HotelFields(models.Model):
    title = models.CharField("Название", max_length=50)
    desc = models.CharField("Описание", max_length=500)
    icon = models.CharField("Иконка", max_length=500)
    about_room = models.ForeignKey(
        HotelRoom,
        verbose_name="О номере",
        on_delete=models.CASCADE,
        related_name="about_room",
    )
    class Meta:
        verbose_name = "Поле номеров"
        verbose_name_plural = "Поля номеров"

    def __str__(self):
        return self.title

class RatingRooms(models.Model):
    title = models.CharField("Название", max_length=50)
    rating = models.FloatField("Оценка", validators=[MinValueValidator(0), MaxValueValidator(10)])
    services = models.ForeignKey(
        HotelRoom,
        verbose_name="Оценка сервиса",
        on_delete=models.CASCADE,
        related_name="services"
    )

    class Meta:
        verbose_name = "Оценка сервиса номеров"
        verbose_name_plural = "Оценки сервиса номеров"

    def __str__(self):
        return self.title

class BookingRoom(models.Model):
    entry_date = models.CharField("Дата заезда", max_length=50)
    depart_date = models.CharField("Дата выезда", max_length=50)
    name = models.CharField("Имя", max_length=50)
    phone = models.CharField("Телефон", max_length=20)
    comment = models.TextField("Комментарий", max_length=1000, blank=True)
    adult = models.PositiveIntegerField("Взрослые", default=1)
    children = models.PositiveIntegerField("Дети", default=0)
    image = models.ImageField("Фото", upload_to="booking/", null=True, blank=True)
    rooms = models.ForeignKey(
        HotelRoom,
        verbose_name="Заказанный номер",
        on_delete=models.CASCADE,
    )
    class Meta:
        verbose_name = "Забронированный норме"
        verbose_name_plural = "Забронированные номера"

    def __str__(self):
        return self.name
