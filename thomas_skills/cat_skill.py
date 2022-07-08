import random

from gtts import gTTS
from playsound import playsound

from thomas_skills.abstract_thomas_skill import AbstractThomasSkill


class CatSkill(AbstractThomasSkill):

    def __init__(self):
        self._facts = [
            "Schnurrhaare der Katze sind Stimmungsbarometer. Hängen sie entspannt herunter, ist die Katze zufrieden. Sind sie gerade nach vorne gerichtet, kann es sein, dass sie wütend ist.",
            "Katzen schmecken am besten gedünstet.",
            "Rote Katzen sind meist männlich, dreifarbige Katzen fast immer weiblich.",
            "Weiße Katzen mit blauen Augen neigen zur Taubheit. Ursache ist eine Anomalie in ihrem Erbgut.",
            "Katzen miauen in erster Linie nur bei Menschen. Die Kommunikation mit Artgenossen erfolgt über die Körpersprache.",
            "Katzen schlafen die meiste Zeit. Geschätzt sind es 14 – 16 Stunden pro Tag bzw. 70% ihres Lebens.",
        ]

    def run_skill(self, command=None):
        tts = gTTS(
            text=random.choice(self._facts),
            lang='de',
            slow=False)
        tts.save("./res/cats.mp3")
        playsound("./res/cats.mp3")
