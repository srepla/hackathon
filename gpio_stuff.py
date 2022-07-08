import platform

if platform.system() == "Linux":
    import RPi.GPIO as GPIO


class GPIOStuff:

    def __init__(self):
        if platform.system() == "Linus":
            GPIO.setwarnings(False)
            GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)
            GPIO.setup(11, GPIO.IN)

    def is_recording(self):
        if platform.system() == "Linux":
            GPIO.output(8, GPIO.HIGH)

    def finished_recording(self):
        if platform.system() == "Linux":
            GPIO.output(8, GPIO.LOW)

    def get_nsfw_state(self):
        if platform.system() == "Linux":
            return GPIO.input(11) == 1
        else:
            return False
