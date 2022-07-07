import RPi.GPIO as GPIO


class NSFWDetector:

    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def get_nsfw_state(self):
        return GPIO.input(22) == GPIO.HIGH
