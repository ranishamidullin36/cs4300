from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()
    duration = models.PositiveIntegerField(help_text='Duration in minutes')

    def __str__(self):
        return self.title


class Seat(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='seats')
    seat_number = models.CharField(max_length=10)
    booking_status = models.BooleanField(default=False)  # False = available, True = booked

    def __str__(self):
        return f"{self.movie.title} - {self.seat_number}"


class Booking(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.movie} - {self.seat}"


@receiver(pre_delete, sender=Booking)
def release_seat_on_booking_delete(sender, instance, **kwargs):
    instance.seat.booking_status = False
    instance.seat.save()
