import platform
from threading import Thread
from time import sleep

from command_interpreter import CommandInterpreter
from command_listener import CommandListener
from hey_thomas_detector import HeyThomasDetector
from temp_hum_sensor import TempHumSensor
from thomas_skills.joke_skill import JokeSkill
from thomas_skills.markus_skill import MarkusSkill
from thomas_skills.temp_skill import TempSkill
from thomas_skills.timer_skill import TimerSkill


class SoulE:

    def __init__(self):

        self._use_indicator = False

        kw_path = []
        if platform.system() == "Darwin":
            kw_path = ["./res/Hey-Thomas_de_mac_v2_1_0.ppn"]
            self._gpio = None
        elif platform.system() == "Linux":
            from gpio_stuff import GPIOStuff

            kw_path = ["./res/Hey-Thomas_de_raspberry-pi_v2_1_0.ppn"]
            self._gpio = GPIOStuff()

        self._hey_thomas_detector = HeyThomasDetector(
            callback=self.process_hey_thomas,
            access_key="RYkVj5ZVY154e1XGTlVy3NU8p1Y241B4QT9ldgRM9xV1b710JqrhXA==",
            model_path="./res/porcupine_params_de.pv",
            keyword_paths=kw_path,
            sensitivities=[0.5],
        )
        self._command_listener = CommandListener()

    def run(self):
        self._hey_thomas_detector.run()

    def process_hey_thomas(self):
        try:
            if self._gpio:
                self._gpio.is_recording()

            command = self._command_listener.from_microphone()
            command_index = CommandInterpreter.process_command(command)

            print("Recognized Command Phrase: %s" % command)

            if self._gpio:
                self._gpio.finished_recording()

            if command_index == 0:
                TempSkill().run_skill()
            elif command_index == 1:
                JokeSkill().run_skill()
            elif command_index == 2:
                TimerSkill().run_skill(command)
            else:
                MarkusSkill().run_skill()

        except Exception as e:
            MarkusSkill().run_skill()
            if self._gpio:
                self._gpio.finished_recording()
            print(e)


if __name__ == '__main__':
    soul_e = Thread(target=SoulE().run)
    soul_e.start()

    temp_hum = None
    if platform.system() == "Linux":
        sleep(10)
        temp_hum = Thread(target=TempHumSensor().run)
        temp_hum.start()

    soul_e.join()
    if temp_hum is not None:
        temp_hum.join()
