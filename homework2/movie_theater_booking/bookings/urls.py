from django.urls import path, include
from rest_framework import routers
from .views import MovieViewSet, SeatViewSet, BookingViewSet
from . import views

router = routers.DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'seats', SeatViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    # API endpoints
    path('api/', include(router.urls)),
    # Template views
    path('', views.movie_list, name='movie_list'),
    path('book/<int:movie_id>/', views.book_seat, name='book_seat'),
    path('history/', views.booking_history, name='booking_history'),
]
