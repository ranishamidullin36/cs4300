from django.db import models

# Create your models here.

class Movie(models.Model):
    title = 
    description = 
    release_date =  
    duration = 


class Seat(models.Model):
    seat_number = 
    booking_status = 


class Booking(models.Model):   
    movie = 
    seat =  
    user =  
    booking_date = 
