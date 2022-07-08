import random

from gtts import gTTS
from playsound import playsound

from gpio_stuff import GPIOStuff


class ThomasFeedbacker:

    def __init__(self):

        self._sfw_phrases = [
            "Hi",
            "Was kann Thomas für dich tun?",
            "Ja Geil!",
            "Thomas ist stehts zu diensten!"
        ]

        self._nsfw_phrases = [
            "Nerv nicht!",
            "Du sollst arbeiten und nicht quatschen!",
            "Mach dein kram alleine, Thomas hat kein bock!",
            "Kündigung ist Raus!"
        ]

        self._nsfw_detector = GPIOStuff()

    def play_feedback_phrase(self):

        nsfw = self._nsfw_detector.get_nsfw_state()

        text = random.choice(self._nsfw_phrases) if nsfw else random.choice(self._sfw_phrases)
        tts = gTTS(text=text,
                   lang='de',
                   slow=False)
        tts.save("./res/feedback.mp3")
        playsound("./res/feedback.mp3")
