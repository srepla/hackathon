from datetime import datetime
import time
from datetime import timedelta
from threading import Thread
from playsound import playsound
from text_to_num import text2num

from thomas_skills.abstract_thomas_skill import AbstractThomasSkill


def alarm(amount):
    print("timer: {} Minuten".format(int(amount)/60))
    start = datetime.now()
    while start + timedelta(seconds=int(amount)) > datetime.now():
        # print("waiting..")
        time.sleep(2)

    playsound("./res/alarm.mp3")


class TimerSkill(AbstractThomasSkill):

    def run_skill(self, command):
        minutes = False
        timer_amount = None
        if "minuten" in command.lower():
            minutes = True
        for item in command.split(" "):
            if item.isdigit():
                timer_amount = item
                break
        if timer_amount is None:
            for item in command.split(" "):
                if text2num(item, "de").isdigit():
                    timer_amount = text2num(item, "de")
                    break

        if minutes:
            timer_amount *= 60

        if timer_amount is not None:
            Thread(target=alarm, args=(timer_amount,)).start()
