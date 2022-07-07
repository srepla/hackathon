from playsound import playsound

from data_store import DataStore
from thomas_skills.abstract_thomas_skill import AbstractThomasSkill


class TempSkill(AbstractThomasSkill):

    def __init__(self):
        self._data_store = DataStore()

    def run_skill(self):
        temp, hum = self._data_store.load_from_db()

        print("temp: {}, hum: {}".format(temp, hum))

        if temp > 25:
            playsound("./res/zu_warm.mp3")
        elif temp <= 25:
            playsound("./res/zu_kalt.mp3")