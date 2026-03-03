from rest_framework import serializers
from .models import Movie, Seat, Booking

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    movie = serializers.StringRelatedField()
    seat = serializers.StringRelatedField()
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Booking
        fields = '__all__'
