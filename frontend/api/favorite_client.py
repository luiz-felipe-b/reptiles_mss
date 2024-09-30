from flask import session
import requests
from . import FAVORITE_API_URL

class FavoriteClient:
    @staticmethod
    def get_favorites():
        headers = {
            'Authorization': session['user_api_key']
        }
        response = requests.get(FAVORITE_API_URL + '/favorite/all', headers=headers)
        return response.json()

    @staticmethod
    def toggle_favorites(reptile_id):
        payload = {
            'reptile_id': reptile_id
        }
        headers = {
            'Authorization': session['user_api_key']
        }
        response = requests.post(FAVORITE_API_URL + '/favorite/toggle', data=payload, headers=headers)
        return response.json()
