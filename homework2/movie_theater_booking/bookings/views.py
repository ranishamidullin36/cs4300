from rest_framework import viewsets
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer


# API ViewSets
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


# Template Views
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'bookings/movie_list.html', {'movies': movies})

def book_seat(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    available_seats = Seat.objects.filter(movie=movie, booking_status=False)
    if request.method == 'POST':
        seat_number = request.POST.get('seat_number')
        seat = get_object_or_404(Seat, movie=movie, seat_number=seat_number, booking_status=False)
        user = request.user if request.user.is_authenticated else User.objects.first()
        if user is None:
            user = User.objects.create_user(username='guest', password='guest123')
        Booking.objects.create(movie=movie, seat=seat, user=user)
        seat.booking_status = True
        seat.save()
        return redirect('booking_history')
    return render(request, 'bookings/seat_booking.html', {
        'movie': movie,
        'available_seats': available_seats,
    })

def booking_history(request):
    bookings = Booking.objects.all().select_related('movie', 'seat', 'user')
    return render(request, 'bookings/booking_history.html', {'bookings': bookings})
