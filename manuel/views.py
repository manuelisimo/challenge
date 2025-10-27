from django.shortcuts import render
from rest_framework import viewsets
from manuel.models import Planet
from manuel.serializers import PlanetSerializer

class PlanetViewSet(viewsets.ModelViewSet):
    serializer_class = PlanetSerializer
    queryset = Planet.objects.all()
