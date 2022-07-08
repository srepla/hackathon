from gtts import gTTS
from playsound import playsound

from data_store import DataStore
from thomas_skills.abstract_thomas_skill import AbstractThomasSkill


class TempSkill(AbstractThomasSkill):

    def __init__(self):
        self._data_store = DataStore()

    def run_skill(self, command=None):

        temp, hum = self._data_store.load_from_db()
        print("temp: {}, hum: {}".format(temp, hum))

        tts = gTTS(text="Es ist %s Grad warm. Die Luftfeuchtigkeit beträgt %s Prozent" % (temp, hum),
                   lang='de',
                   slow=False)
        tts.save("./res/temp.mp3")
        playsound("./res/temp.mp3")

        if temp > 27:
            playsound("./res/zu_warm.mp3")
        elif temp <= 10:
            playsound("./res/zu_kalt.mp3")
