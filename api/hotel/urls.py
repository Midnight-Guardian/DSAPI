from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

urlpatterns = [
    path('', views.HotelRoomsList.as_view()),
    path('create/', views.BookingRoomRecord.as_view()),
    path('bookinglist/', views.BookingRoomList.as_view()),
    path('list/', views.HotelView.as_view()),
    path('record/', views.BookingRoomRecordView.as_view()),
    path('detail/<int:pk>', views.HotelRoomView.as_view()),
]
router = DefaultRouter()
router.register(r'rooms', views.HotelViewsets, basename='rooms')
urlpatterns +=router.urls