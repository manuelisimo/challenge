from django.test import TestCase
from manuel.helpers.planet_api import PlanetApi
from manuel.models import Planet


class PlanetApiTestCase(TestCase):
    """
    This mainly tests our helper doesn't have any issues querying graphql
    """
    api = None
    def setUp(self):
        self.api = PlanetApi()

    def test_api_query_works(self):
        simple_query = """query {
          planet (id: "cGxhbmV0czox") {
            id name
          }}"""
        result = self.api.get_query(simple_query)
        self.assertEqual(result['planet']['name'], "Tatooine")

class PlanetTestCase(TestCase):
    """
    Basic health check
    """
    def setUp(self):
        pass

    def test_can_save(self):
        earth = Planet(name='Earth')
        earth.save()
        self.assertEqual(Planet.objects.filter(name='Earth').exists(), True)
