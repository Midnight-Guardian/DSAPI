from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from backendapps.hotel.models import HotelRoom, BookingRoom
from .serializers import HotelRoomsSerializer, BookingRoomListSerializer, BookingRoomSerializer


class HotelRoomsList(generics.ListAPIView):
    """Hotel Rooms List"""

    permission_classes = [permissions.AllowAny]
    queryset = HotelRoom.objects.all()
    serializer_class = HotelRoomsSerializer


class BookingRoomList(generics.ListAPIView):
    """Booking Rooms List"""
    permission_classes = [permissions.AllowAny]
    queryset = BookingRoom.objects.all()
    serializer_class = BookingRoomListSerializer


class BookingRoomRecord(generics.CreateAPIView):
    """Booking Room Record"""
    permission_classes = [permissions.AllowAny]
    queryset = BookingRoom.objects.all()
    serializer_class = BookingRoomSerializer


class HotelView(APIView):
    """Hotel Room List"""

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        rooms = HotelRoom.objects.all()
        ser = HotelRoomsSerializer(rooms, many=True)
        return Response(ser.data)


# class BookingRoomRecordView(APIView):
#     def post(self, request):
#         room = BookingRoomSerializer(data=request.data)
#         print(request.data)
#         if room.is_valid(raise_exception=True):
#             room.save()
#         return Response(room.data, status=201)


class BookingRoomRecordView(generics.ListCreateAPIView):
    """Booking Room list and record"""
    permission_classes = [permissions.IsAuthenticated]
    queryset = BookingRoom.objects.all()
    serializer_class = BookingRoomSerializer


class HotelRoomView(generics.RetrieveAPIView):
    """Hotel Room detail"""
    permission_classes = [permissions.AllowAny]
    queryset = HotelRoom.objects.all()
    serializer_class = HotelRoomsSerializer


class HotelViewsets(viewsets.ViewSet):
    """Hotel Rooms list and detail"""
    def list(self, request):
        queryset = HotelRoom.objects.all()
        serializer = HotelRoomsSerializer(queryset, many=True)
        return Response(serializer.data, status=200)

    def retrieve(self, request, pk=None):
        queryset = HotelRoom.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = HotelRoomsSerializer(user)
        return Response(serializer.data)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]
