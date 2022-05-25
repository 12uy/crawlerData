import json

import requests


def textToSpeech(payload):
    url = 'https://api.fpt.ai/hmi/tts/v5'

    payload = payload.replace("\n", " ")

    api_key = 'Kocbjccgncwa3hFKdXdr0rx2ANUEGAYk' # api key lấy từ fpt.ai

    headers = {
        'api-key': api_key,
        'speed': '',
        'voice': 'banmai'
    }

    response = requests.request('POST', url, data=payload.encode('utf-8'), headers=headers).json()
    linkTTS = response['async']  # lấy ra link mp3 từ json trả về
    return linkTTS



