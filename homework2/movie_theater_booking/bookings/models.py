from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()
    duration = models.PositiveIntegerField(help_text='Duration in minutes')

    def __str__(self):
        return self.title


class Seat(models.Model):
    seat_number = models.CharField(max_length=10)
    booking_status = models.BooleanField(default=False)  # False = available, True = booked

    def __str__(self):
        return self.seat_number


class Booking(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.movie} - {self.seat}"
