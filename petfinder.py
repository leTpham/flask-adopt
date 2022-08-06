import os
from flask import Flask, render_template, request
import requests

from dotenv import load_dotenv
load_dotenv()


PETFINDER_API_KEY = os.environ['PETFINDER_API_KEY']
PETFINDER_SECRET_KEY = os.environ['PETFINDER_SECRET_KEY']

API_BASE_URL = "https://api.petfinder.com/v2"

app = Flask(__name__)


def update_auth_token_string():
    resp = requests.post(
        f"{API_BASE_URL}/oauth2/token",
        data={
            "grant_type": "client_credentials",
            "client_id": PETFINDER_API_KEY,
            "client_secret": PETFINDER_SECRET_KEY
        }
    )
    token = resp.json()
    return f"{token['token_type']} {token['access_token']}"



def show_random_pet(auth_token):
    response = requests.get(f"{API_BASE_URL}/animals",
                           headers={"Authorization": auth_token},
                           params={"limit": 100})

    animals = response.json()['animals']
    animal = animals[0]

    return {
        'name': animal['name'],
        'age': animal['age'],
        'photo_url': animal['photos'][0]['large']}
