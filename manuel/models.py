from django.db import models


class Planet(models.Model):
    """
    Planet model. There are some extra fields commented out in case we need to add
    more fields from the graphql datasource in the future
    """
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    # diameter = models.IntegerField()
    # rotation_period = models.IntegerField()
    # orbital_period = models.IntegerField()
    # gravity = models.CharField(max_length=100)
    population = models.FloatField(blank=True, default=None, null=True)
    climates = models.CharField(max_length=100, blank=True, default=None, null=True)
    terrains = models.CharField(max_length=100, blank=True, default=None, null=True)
    # surface_water = models.FloatField()
    # residents
    # films
    created = models.DateTimeField(auto_now_add=True)
