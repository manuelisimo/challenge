from django.core.management.base import BaseCommand
from manuel.helpers.planet_api import PlanetApi
from manuel.serializers import PlanetSerializer
from manuel.models import Planet
import logging

logger = logging.getLogger("challenge")

class Command(BaseCommand):
    """
    Import the planets from the graphql external source
    """

    def handle(self, *args, **options):
        planet_api = PlanetApi()
        all_planets = planet_api.get_all_planets()
        logger.debug("These are all the planets")
        logger.debug(all_planets)

        for planet in all_planets:
            logger.debug(planet)
            try:
                if not Planet.objects.filter(id=planet['id']).exists():
                    serializer = PlanetSerializer(data=planet)
                    if not serializer.is_valid():
                        logger.debug("Invalid planet")
                        logger.debug(planet)
                    serializer.save()
            except:
                continue