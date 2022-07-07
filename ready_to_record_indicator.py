import platform

if platform.system() == "Linux":
    import RPi.GPIO as GPIO


class StatusIndicator:

    def __init__(self):
        if platform.system() == "Linux":
            GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)

    def is_recording(self):
        GPIO.output(8, GPIO.HIGH)

    def finished_recording(self):
        GPIO.output(8, GPIO.LOW)
