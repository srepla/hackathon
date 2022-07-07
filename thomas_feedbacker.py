import random

from gtts import gTTS
from playsound import playsound


class ThomasFeedbacker:

    def __init__(self):
        self.nsfw = False

        self._sfw_phrases = [
            "Hi",
            "Was kann Thomas für dich tun?",
            "Ja Geil!",
            "Thomas ist stehts zu diensten!"
        ]

        self._nsfw_phrases = [
            "Nerv nicht!",
            "Du sollst arbeiten und nicht quatschen!",
            "Mach dein kram alleine, Thomas hat kein bock!"
            "Kündigung ist Raus!"
        ]

    def play_feedback_phrase(self):
        text = random.choice(self._nsfw_phrases) if self.nsfw else random.choice(self._sfw_phrases)
        tts = gTTS(text=text,
                   lang='de',
                   slow=False)
        tts.save("./res/feedback.mp3")
        playsound("./res/feedback.mp3")
