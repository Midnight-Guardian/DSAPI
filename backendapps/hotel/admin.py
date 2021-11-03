from django.contrib import admin
from .models import HotelRoom, HotelFields, RatingRooms, BookingRoom
# Register your models here.
admin.site.register(HotelRoom)
admin.site.register(HotelFields)
admin.site.register(RatingRooms)
admin.site.register(BookingRoom)
