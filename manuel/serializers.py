from rest_framework import serializers
from manuel.models import Planet, Book

class PlanetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planet
        fields = ["id", "name", "population", "climates", "terrains"]

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "title"]
