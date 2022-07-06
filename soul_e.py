import platform

from playsound import playsound

from command_interpreter import CommandInterpreter
from command_listener import CommandListener
from hey_thomas_detector import HeyThomasDetector
from temp_hum_reader import TempHumReader


class SoulE:

    def __init__(self):

        if platform.system() == "Darwin":
            self._hey_thomas_detector = HeyThomasDetector(
                callback=self.process_hey_thomas,
                access_key="RYkVj5ZVY154e1XGTlVy3NU8p1Y241B4QT9ldgRM9xV1b710JqrhXA==",
                model_path="./res/porcupine_params_de.pv",
                keyword_paths=["./res/Hey-Thomas_de_mac_v2_1_0.ppn"],
                sensitivities=[0.5],
            )

        elif platform.system() == "Linux":
            self._hey_thomas_detector = HeyThomasDetector(
                callback=self.process_hey_thomas,
                access_key="RYkVj5ZVY154e1XGTlVy3NU8p1Y241B4QT9ldgRM9xV1b710JqrhXA==",
                model_path="./res/porcupine_params_de.pv",
                keyword_paths=["./res/Hey-Thomas_de_raspberry-pi_v2_1_0.ppn"],
                sensitivities=[0.5],
            )

            self._command_listener = CommandListener()

    def run(self):
        self._hey_thomas_detector.run()

    def process_hey_thomas(self):
        command = self._command_listener.from_microphone()
        print(command)
        command_index = CommandInterpreter.process_command(command)
        if command_index == 0:
            temp, hum = TempHumReader.read()
            print("temp: {}, hum: {}".format(temp, hum))
            if temp > 25:
                playsound("./res/zu_warm.mp3")
            elif temp <= 25:
                playsound("./res/zu_kalt.mp3")


if __name__ == '__main__':
    SoulE().run()
