import platform

import speech_recognition as sr
import sounddevice as sd
import numpy as np
from gtts import gTTS
from playsound import playsound

# speech_engine = sr.Recognizer()


# def print_sound(indata, outdata, frames, time, status):
#     volume_norm = np.linalg.norm(indata) * 10
#     print("|" * int(volume_norm))
#
#
# def from_microphone():
#     with sr.Microphone() as micro:
#         print("Recording...")
#         audio = speech_engine.record(micro, duration=5)
#         print("Recognition...")
#         text = speech_engine.recognize_google(audio, language="de-DE")
#         return text


import webbrowser




if __name__ == '__main__':
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

    webbrowser.open(url, new=0, autoraise=True)


    #print(platform.system())
    # print(from_microphone())
    # with sd.Stream(callback=print_sound):
    #     sd.sleep(10000)

    # language = 'de'
    # tts = gTTS(text="Es ist arsch kalt! So kann man nicht arbeiten!",
    #            lang=language,
    #            slow=False)
    # tts.save("./res/zu_kalt.mp3")
    # playsound("./res/zu_kalt.mp3")
