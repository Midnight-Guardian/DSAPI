from rest_framework import serializers
from backendapps.hotel.models import HotelFields, HotelRoom, RatingRooms, BookingRoom

class HotelFieldsSerializer(serializers.ModelSerializer):
    """Hotel fields serializer"""

    class Meta:
        model = HotelFields
        fields = (
            "title",
            "desc",
            "icon",
        )

class RatingsRoomsSerializer(serializers.ModelSerializer):
    """Ratings Rooms Serializer"""

    class Meta:
        model = RatingRooms
        fields = (
            "title",
            "rating",
        )

class HotelRoomsSerializer(serializers.ModelSerializer):
    """Hotel Rooms Serializer"""

    about_room = HotelFieldsSerializer(many=True)
    services = RatingsRoomsSerializer(many=True)
    image = serializers.ImageField(use_url=True)
    class Meta:
        model = HotelRoom
        fields = (
            "id",
            "title",
            "desc",
            "image",
            "about_room",
            "services"
        )

class BookingHotelSerializer(serializers.ModelSerializer):
    """Booking Hotel Room Serializer"""

    class Meta:
        model = HotelRoom
        fields = ("id", "title")


class BookingRoomListSerializer(serializers.ModelSerializer):
    """Booking Rooms List Serializer"""
    rooms = BookingHotelSerializer(read_only=True)

    class Meta:
        model = BookingRoom
        fields = (
            "entry_date",
            "depart_date",
            "name",
            "phone",
            "comment",
            "adult",
            "children",
            "rooms",
            "image"
        )


class BookingRoomSerializer(serializers.ModelSerializer):
    """Booking Room Serializer"""

    class Meta:
        model = BookingRoom
        fields = (
            "entry_date",
            "depart_date",
            "name",
            "phone",
            "comment",
            "adult",
            "children",
            "rooms",
            "image",
        )

    # Требуется в случае CreateApiView
    def create(self, request):
        """Record creation in database"""
        print(request)
        results = request.pop('rooms')
        booking = BookingRoom.objects.create(rooms=results, **request)
        return booking