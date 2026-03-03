from django.urls import path, include
from rest_framework import routers
from .views import MovieViewSet, SeatViewSet, BookingViewSet

router = routers.DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'seats', SeatViewSet)
router.register(r'bookings', BookingViewSet)

from . import views

urlpatterns = [
    path('', include(router.urls)),
    path('movies/', views.movie_list, name='movie_list'),
    path('book-seat/<int:movie_id>/', views.seat_booking, name='book_seat'),
    path('booking-history/', views.booking_history, name='booking_history'),
]
