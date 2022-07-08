from gtts import gTTS
from playsound import playsound

from thomas_skills.abstract_thomas_skill import AbstractThomasSkill


class MarkusSkill(AbstractThomasSkill):

    def run_skill(self, command=None):
        tts = gTTS(text="Ich versteh die Frage nicht.",
                   lang='de',
                   slow=False)
        tts.save("./res/ivdfn.mp3")
        playsound("./res/ivdfn.mp3")
