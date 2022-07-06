import speech_recognition as sr


class CommandListener:

    def __init__(self):
        self._speech_engine = sr.Recognizer()

    def from_microphone(self):
        with sr.Microphone() as micro:
            print("Recording...")
            audio = self._speech_engine.record(micro, duration=5)
            print("Recognition...")
            text = self._speech_engine.recognize_google(audio, language="de-DE")
            return text
