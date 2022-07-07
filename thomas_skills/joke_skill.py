import json

import requests
from gtts import gTTS
from playsound import playsound

from thomas_skills.abstract_thomas_skill import AbstractThomasSkill


class JokeSkill(AbstractThomasSkill):

    def run_skill(self, command=None):
        joke_response = requests.get('https://witzapi.de/api/joke')
        joke_text = json.loads(joke_response.text)
        print(joke_text[0]['text'])
        tts = gTTS(text=joke_text[0]['text'],
                   lang='de',
                   slow=False)
        tts.save("./res/joke.mp3")
        playsound("./res/joke.mp3")