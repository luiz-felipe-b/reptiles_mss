import requests

from . import REPTILE_API_URL

class ReptileClient:

    @staticmethod
    def get_reptiles():
        response = requests.get(REPTILE_API_URL + '/reptile/all')
        return response.json()

    @staticmethod
    def get_reptile(slug):
        response = requests.get(REPTILE_API_URL + '/reptile/' + slug)
        return response.json()
