from behave import given, when, then
from django.contrib.auth.models import User
from bookings.models import Movie, Seat, Booking


@given('there is a movie "{title}" in the system')
def step_create_movie(context, title):
    context.movie = Movie.objects.create(
        title=title, description='A great movie',
        release_date='2023-01-01', duration=120
    )


@given('there is an available seat "{seat_number}"')
def step_create_seat(context, seat_number):
    context.seat = Seat.objects.create(seat_number=seat_number, booking_status=False)


@given('there is a user "{username}"')
def step_create_user(context, username):
    context.user = User.objects.create_user(username=username, password='pass123')


@given('"{username}" has booked seat "{seat_number}" for "{movie_title}"')
def step_create_booking(context, username, seat_number, movie_title):
    user = User.objects.get(username=username)
    movie = Movie.objects.get(title=movie_title)
    seat = Seat.objects.get(seat_number=seat_number)
    Booking.objects.create(user=user, movie=movie, seat=seat)


@when('I request the movie list from the API')
def step_request_movie_list(context):
    context.response = context.test.client.get('/api/movies/')


@when('I book seat "{seat_number}" for movie "{movie_title}" as "{username}"')
def step_book_seat_api(context, seat_number, movie_title, username):
    movie = Movie.objects.get(title=movie_title)
    seat = Seat.objects.get(seat_number=seat_number)
    context.response = context.test.client.post('/api/bookings/', {
        'movie': movie.id,
        'seat': seat.id,
        'user': username,
    }, content_type='application/json')


@when('I request the booking list from the API')
def step_request_booking_list(context):
    context.response = context.test.client.get('/api/bookings/')


@when('I visit the movie list page')
def step_visit_movie_list(context):
    context.response = context.test.client.get('/')


@when('I visit the seat booking page for "{movie_title}"')
def step_visit_seat_booking(context, movie_title):
    movie = Movie.objects.get(title=movie_title)
    context.response = context.test.client.get(f'/book/{movie.id}/')


@then('I should see "{text}" in the response')
def step_check_response_contains(context, text):
    assert text in str(context.response.content), f"'{text}' not found in response"


@then('the booking should be created successfully')
def step_check_booking_created(context):
    assert context.response.status_code == 201, f"Expected 201, got {context.response.status_code}"
    assert Booking.objects.count() == 1


@then('I should see a booking for "{username}"')
def step_check_booking_for_user(context, username):
    assert username in str(context.response.content)


@then('I should see "{text}" on the page')
def step_check_page_contains(context, text):
    assert context.response.status_code == 200
    assert text in str(context.response.content)


@then('I should see the booking form')
def step_check_booking_form(context):
    assert context.response.status_code == 200
    assert 'form' in str(context.response.content).lower()


@then('I should see seat "{seat_number}" as available')
def step_check_seat_available(context, seat_number):
    assert seat_number in str(context.response.content)
