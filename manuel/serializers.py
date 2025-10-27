from rest_framework import serializers
from manuel.models import Planet

class PlanetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planet
        fields = ["id", "name", "population", "climates", "terrains"]
