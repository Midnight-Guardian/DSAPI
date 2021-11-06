from django.contrib import admin
from .models import HotelRoom, HotelFields, RatingRooms, BookingRoom
# Register your models here.
admin.site.register(HotelFields)

class HotelFieldsAdmin(admin.StackedInline):
    model = HotelFields
    extra = 1
    show_change_link = True


class RatingsRoomAdmin(admin.StackedInline):
    model = RatingRooms
    extra = 1
    show_change_link = True

@admin.register(HotelRoom)
class HotelRoomAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc')
    search_fields = ('title',)
    inlines = [HotelFieldsAdmin, RatingsRoomAdmin]

@admin.register(BookingRoom)
class BookingRoomAdmin(admin.ModelAdmin):
    list_display = ("name", 'phone', "entry_date", "depart_date", "adult", "children",)
    search_fields = ("name", )