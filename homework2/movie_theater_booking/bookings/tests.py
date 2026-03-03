from django.test import TestCase
from django.contrib.auth.models import User
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer

class MovieModelTest(TestCase):
    def test_movie_creation(self):
        movie = Movie.objects.create(title='Test Movie', description='Desc', release_date='2023-01-01', duration=120)
        self.assertEqual(str(movie), 'Test Movie')

class SeatModelTest(TestCase):
    def test_seat_creation(self):
        seat = Seat.objects.create(seat_number='A1', booking_status=False)
        self.assertEqual(str(seat), 'A1')

class BookingModelTest(TestCase):
    def test_booking_creation(self):
        user = User.objects.create(username='testuser')
        movie = Movie.objects.create(title='Test Movie', description='Desc', release_date='2023-01-01', duration=120)
        seat = Seat.objects.create(seat_number='A1', booking_status=False)
        booking = Booking.objects.create(user=user, movie=movie, seat=seat)
        self.assertIn('testuser', str(booking))

class MovieSerializerTest(TestCase):
    def test_movie_serializer(self):
        movie = Movie.objects.create(title='Test Movie', description='Desc', release_date='2023-01-01', duration=120)
        serializer = MovieSerializer(movie)
        self.assertEqual(serializer.data['title'], 'Test Movie')

class SeatSerializerTest(TestCase):
    def test_seat_serializer(self):
        seat = Seat.objects.create(seat_number='A1', booking_status=False)
        serializer = SeatSerializer(seat)
        self.assertEqual(serializer.data['seat_number'], 'A1')

class BookingSerializerTest(TestCase):
    def test_booking_serializer(self):
        user = User.objects.create(username='testuser')
        movie = Movie.objects.create(title='Test Movie', description='Desc', release_date='2023-01-01', duration=120)
        seat = Seat.objects.create(seat_number='A1', booking_status=False)
        booking = Booking.objects.create(user=user, movie=movie, seat=seat)
        serializer = BookingSerializer(booking)
        self.assertEqual(serializer.data['user'], 'testuser')

from rest_framework.test import APIClient
from django.urls import reverse

class MovieViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.movie = Movie.objects.create(title='Test Movie', description='Desc', release_date='2023-01-01', duration=120)

    def test_movie_list(self):
        response = self.client.get(reverse('movie-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['title'], 'Test Movie')

class SeatViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.seat = Seat.objects.create(seat_number='A1', booking_status=False)

    def test_seat_list(self):
        response = self.client.get(reverse('seat-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['seat_number'], 'A1')

class BookingViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(username='testuser')
        self.movie = Movie.objects.create(title='Test Movie', description='Desc', release_date='2023-01-01', duration=120)
        self.seat = Seat.objects.create(seat_number='A1', booking_status=False)
        self.booking = Booking.objects.create(user=self.user, movie=self.movie, seat=self.seat)

    def test_booking_list(self):
        response = self.client.get(reverse('booking-list'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('testuser', str(response.data[0]['user']))
