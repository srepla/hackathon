import platform

from command_interpreter import CommandInterpreter
from command_listener import CommandListener
from hey_thomas_detector import HeyThomasDetector
from ready_to_record_indicator import ReadyToRecordIndicator
from thomas_skills.joke_skill import JokeSkill
from thomas_skills.temp_skill import TempSkill


class SoulE:

    def __init__(self):

        self._use_indicator = False

        kw_path = []
        if platform.system() == "Darwin":
            kw_path = ["./res/Hey-Thomas_de_mac_v2_1_0.ppn"]
            self._indicator = None
        elif platform.system() == "Linux":
            kw_path = ["./res/Hey-Thomas_de_raspberry-pi_v2_1_0.ppn"]
            self._indicator = ReadyToRecordIndicator()

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
            if self._indicator:
                self._indicator.is_recording()

            command = self._command_listener.from_microphone()
            command_index = CommandInterpreter.process_command(command)

            print("Recognized Command Phrase: %s" % command)

            if self._indicator:
                self._indicator.finished_recording()

            if command_index == 0:
                TempSkill().run_skill()
            elif command_index == 1:
                JokeSkill().run_skill()

        except Exception as e:
            print(e)


if __name__ == '__main__':
    SoulE().run()
