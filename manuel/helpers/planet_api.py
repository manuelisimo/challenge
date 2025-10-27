import requests
import json
import logging
from requests_toolbelt.utils import dump

logger = logging.getLogger('challenge')

class PlanetApi:
    base_url = 'https://swapi-graphql.netlify.app/graphql'
    _request = None

    def get_query(self, query):
        """
        Generic query method for this graphql api
        """
        logger.debug(f'graphql query: {query}')
        self._request = requests.get(self.base_url, params={'query': query})
        logger.debug(dump.dump_all(self._request).decode('utf-8'))
        if self._request.status_code >= 299:
            raise Exception
        return json.loads(self._request.content)['data']

    def get_all_planets(self):
        """
        This builds a query to get all the planets
        """
        query = """query {
            allPlanets {
                planets {
                    id
                    name 
                    population
                    terrains 
                    climates
                }
            }
        }"""

        return self.get_query(query)['allPlanets']['planets']
