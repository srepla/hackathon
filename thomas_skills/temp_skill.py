from playsound import playsound

from temp_hum_reader import TempHumReader
from thomas_skills.abstract_thomas_skill import AbstractThomasSkill


class TempSkill(AbstractThomasSkill):

    def __init__(self):
        self._temp_hum_reader = TempHumReader()

    def run_skill(self):
        temp, hum = self._temp_hum_reader.read()
        print("temp: {}, hum: {}".format(temp, hum))
        if temp > 25:
            playsound("./res/zu_warm.mp3")
        elif temp <= 25:
            playsound("./res/zu_kalt.mp3")