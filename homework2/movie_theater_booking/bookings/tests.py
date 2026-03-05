from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APIClient
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer


# ===== Model Tests =====
class MovieModelTest(TestCase):
    def test_movie_creation(self):
        movie = Movie.objects.create(title='Test Movie', description='Desc', release_date='2023-01-01', duration=120)
        self.assertEqual(str(movie), 'Test Movie')

    def test_movie_fields(self):
        movie = Movie.objects.create(title='Test Movie', description='A great movie', release_date='2023-06-15', duration=90)
        self.assertEqual(movie.title, 'Test Movie')
        self.assertEqual(movie.description, 'A great movie')
        self.assertEqual(movie.duration, 90)


class SeatModelTest(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(title='Test Movie', description='Desc', release_date='2023-01-01', duration=120)

    def test_seat_creation(self):
        seat = Seat.objects.create(seat_number='A1', booking_status=False, movie=self.movie)
        self.assertEqual(str(seat), 'Test Movie - A1')

    def test_seat_default_status(self):
        seat = Seat.objects.create(seat_number='B2', movie=self.movie)
        self.assertFalse(seat.booking_status)


class BookingModelTest(TestCase):
    def test_booking_creation(self):
        user = User.objects.create(username='testuser')
        movie = Movie.objects.create(title='Test Movie', description='Desc', release_date='2023-01-01', duration=120)
        seat = Seat.objects.create(seat_number='A1', booking_status=False, movie=movie)
        booking = Booking.objects.create(user=user, movie=movie, seat=seat)
        self.assertIn('testuser', str(booking))

    def test_booking_str(self):
        user = User.objects.create(username='john')
        movie = Movie.objects.create(title='Avatar', description='Desc', release_date='2023-01-01', duration=120)
        seat = Seat.objects.create(seat_number='C3', movie=movie)
        booking = Booking.objects.create(user=user, movie=movie, seat=seat)
        self.assertIn('Avatar', str(booking))
        self.assertIn('C3', str(booking))


# ===== Serializer Tests =====
class MovieSerializerTest(TestCase):
    def test_movie_serializer(self):
        movie = Movie.objects.create(title='Test Movie', description='Desc', release_date='2023-01-01', duration=120)
        serializer = MovieSerializer(movie)
        self.assertEqual(serializer.data['title'], 'Test Movie')

    def test_movie_serializer_contains_all_fields(self):
        movie = Movie.objects.create(title='Test', description='Desc', release_date='2023-01-01', duration=90)
        serializer = MovieSerializer(movie)
        self.assertIn('id', serializer.data)
        self.assertIn('title', serializer.data)
        self.assertIn('description', serializer.data)
        self.assertIn('release_date', serializer.data)
        self.assertIn('duration', serializer.data)


class SeatSerializerTest(TestCase):
    def test_seat_serializer(self):
        movie = Movie.objects.create(title='Test Movie', description='Desc', release_date='2023-01-01', duration=120)
        seat = Seat.objects.create(seat_number='A1', booking_status=False, movie=movie)
        serializer = SeatSerializer(seat)
        self.assertEqual(serializer.data['seat_number'], 'A1')


class BookingSerializerTest(TestCase):
    def test_booking_serializer(self):
        user = User.objects.create(username='testuser')
        movie = Movie.objects.create(title='Test Movie', description='Desc', release_date='2023-01-01', duration=120)
        seat = Seat.objects.create(seat_number='A1', booking_status=False, movie=movie)
        booking = Booking.objects.create(user=user, movie=movie, seat=seat)
        serializer = BookingSerializer(booking)
        self.assertEqual(serializer.data['user'], 'testuser')


# ===== API ViewSet Tests =====
class MovieViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.movie = Movie.objects.create(title='Test Movie', description='Desc', release_date='2023-01-01', duration=120)

    def test_movie_list(self):
        response = self.client.get(reverse('movie-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['title'], 'Test Movie')

    def test_movie_create(self):
        data = {'title': 'New Movie', 'description': 'New Desc', 'release_date': '2024-01-01', 'duration': 150}
        response = self.client.post(reverse('movie-list'), data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Movie.objects.count(), 2)

    def test_movie_detail(self):
        response = self.client.get(reverse('movie-detail', args=[self.movie.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], 'Test Movie')

    def test_movie_update(self):
        data = {'title': 'Updated Movie', 'description': 'Desc', 'release_date': '2023-01-01', 'duration': 120}
        response = self.client.put(reverse('movie-detail', args=[self.movie.id]), data, format='json')
        self.assertEqual(response.status_code, 200)
        self.movie.refresh_from_db()
        self.assertEqual(self.movie.title, 'Updated Movie')

    def test_movie_delete(self):
        response = self.client.delete(reverse('movie-detail', args=[self.movie.id]))
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Movie.objects.count(), 0)


class SeatViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.movie = Movie.objects.create(title='Test Movie', description='Desc', release_date='2023-01-01', duration=120)
        self.seat = Seat.objects.create(seat_number='A1', booking_status=False, movie=self.movie)

    def test_seat_list(self):
        response = self.client.get(reverse('seat-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['seat_number'], 'A1')

    def test_seat_create(self):
        data = {'seat_number': 'B2', 'booking_status': False, 'movie': self.movie.id}
        response = self.client.post(reverse('seat-list'), data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Seat.objects.count(), 2)


class BookingViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(username='testuser')
        self.movie = Movie.objects.create(title='Test Movie', description='Desc', release_date='2023-01-01', duration=120)
        self.seat = Seat.objects.create(seat_number='A1', booking_status=False, movie=self.movie)
        self.booking = Booking.objects.create(user=self.user, movie=self.movie, seat=self.seat)

    def test_booking_list(self):
        response = self.client.get(reverse('booking-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['user'], 'testuser')

    def test_booking_create(self):
        seat2 = Seat.objects.create(seat_number='B2', booking_status=False, movie=self.movie)
        data = {'movie': self.movie.id, 'seat': seat2.id, 'user': 'testuser'}
        response = self.client.post(reverse('booking-list'), data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Booking.objects.count(), 2)


# ===== Template View Tests =====
class MovieListViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.movie = Movie.objects.create(title='Test Movie', description='Desc', release_date='2023-01-01', duration=120)

    def test_movie_list_view(self):
        response = self.client.get(reverse('movie_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Movie')
        self.assertTemplateUsed(response, 'bookings/movie_list.html')

    def test_movie_list_empty(self):
        Movie.objects.all().delete()
        response = self.client.get(reverse('movie_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No movies available')


class BookSeatViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.movie = Movie.objects.create(title='Test Movie', description='Desc', release_date='2023-01-01', duration=120)
        self.seat = Seat.objects.create(seat_number='A1', booking_status=False, movie=self.movie)

    def test_book_seat_get(self):
        response = self.client.get(reverse('book_seat', args=[self.movie.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Movie')
        self.assertTemplateUsed(response, 'bookings/seat_booking.html')

    def test_book_seat_post(self):
        response = self.client.post(reverse('book_seat', args=[self.movie.id]), {'seat_number': 'A1'})
        self.assertEqual(response.status_code, 302)
        self.seat.refresh_from_db()
        self.assertTrue(self.seat.booking_status)
        self.assertEqual(Booking.objects.count(), 1)

    def test_book_seat_invalid_movie(self):
        response = self.client.get(reverse('book_seat', args=[999]))
        self.assertEqual(response.status_code, 404)


class BookingHistoryViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(username='testuser')
        self.movie = Movie.objects.create(title='Test Movie', description='Desc', release_date='2023-01-01', duration=120)
        self.seat = Seat.objects.create(seat_number='A1', booking_status=True, movie=self.movie)
        self.booking = Booking.objects.create(user=self.user, movie=self.movie, seat=self.seat)

    def test_booking_history_view(self):
        response = self.client.get(reverse('booking_history'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Movie')
        self.assertTemplateUsed(response, 'bookings/booking_history.html')

    def test_booking_history_empty(self):
        Booking.objects.all().delete()
        response = self.client.get(reverse('booking_history'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No bookings found')
