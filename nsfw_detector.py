import RPi.GPIO as GPIO


class NSFWDetector:

    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(11, GPIO.IN)

    def get_nsfw_state(self):
        return GPIO.input(11) == 1
