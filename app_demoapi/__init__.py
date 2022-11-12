from flask import Flask, request
import requests
from functools import lru_cache
from app_demoapi.settings import settings

app = Flask(__name__)


@lru_cache(maxsize=128)
def summ(payload):
    API_URL = "https://api-inference.huggingface.co/models/sshleifer/distilbart-cnn-12-6"
    headers = {"Authorization": f"Bearer {settings.HF_TOKEN}"}
    query = {"inputs": payload}
    response = requests.post(API_URL, headers=headers, json=query)
    return response.json()


@app.route('/summ/', methods=['POST'])
def summ_route():
    body = request.json
    payload = body["text"]
    output = summ(payload)
    return output


@lru_cache(maxsize=128)
def textgen(payload):
    API_URL = "https://api-inference.huggingface.co/models/gpt2"
    headers = {"Authorization": f"Bearer {settings.HF_TOKEN}"}
    query = {"inputs": payload}
    response = requests.post(API_URL, headers=headers, json=query)
    return response.json()


@app.route('/textgen/', methods=['POST'])
def textgen_route():
    body = request.json
    payload = body["text"]
    output = textgen(payload)
    return output


# @lru_cache(maxsize=128)
# def punctrestore(payload):
#     headers = {"Authorization": f"Bearer {settings.HF_TOKEN}"}
#     query = {"inputs": payload}
#     response = requests.post(API_URL, headers=headers, json=query)
#     return response.json()
#
#
# @app.route('/punctrestore', methods=['POST'])
# def punctrestore_route(payload):
#     body = request.json
#     payload = body["text"]
#     output = punctrestore(payload)
#     return output


@lru_cache(maxsize=128)
def sentiment(payload: str):
    API_URL = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"
    headers = {"Authorization": f"Bearer {settings.HF_TOKEN}"}
    query = {"inputs": payload}
    response = requests.post(API_URL, headers=headers, json=query)
    return response.json()


@app.route('/sentiment/', methods=['POST'])
def sentiment_route():
    body = request.json
    payload = body["text"]
    output = sentiment(payload)
    return output
