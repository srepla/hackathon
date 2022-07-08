from gtts import gTTS
from playsound import playsound

from thomas_skills.abstract_thomas_skill import AbstractThomasSkill


class ValuesSkill(AbstractThomasSkill):

    def run_skill(self, command=None):
        tts = gTTS(text="Die AdSoul Werte sind: Teamwörk, Transparenz, Selbstbestimmtheit, Verantwortung, Agilität und Alkoholismus.",
                   lang='de',
                   slow=False)
        tts.save("./res/values.mp3")
        playsound("./res/values.mp3")
