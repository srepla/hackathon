import platform

if platform.system() == "Linux":
    import RPi.GPIO as GPIO


class GPIOStuff:

    def __init__(self):
        if platform.system() == "Linux":
            GPIO.setwarnings(False)
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(14, GPIO.OUT, initial=GPIO.LOW)
            GPIO.setup(17, GPIO.IN)

    def is_recording(self):
        if platform.system() == "Linux":
            GPIO.output(14, GPIO.HIGH)

    def finished_recording(self):
        if platform.system() == "Linux":
            GPIO.output(14, GPIO.LOW)

    def get_nsfw_state(self):
        if platform.system() == "Linux":
            return GPIO.input(17) == 1
        else:
            return False
