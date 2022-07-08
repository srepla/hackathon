import platform
from time import sleep

from data_store import DataStore


class TempHumSensor:

    def __init__(self):
        self._data_store = DataStore()

        if platform.system() == "Linux":
            import board
            import adafruit_dht

            self._dht_device = adafruit_dht.DHT22(board.D4)

        if platform.system() == "Darwin":
            self._data_store.store_in_db(20, 50)

    def run(self):
        if platform.system() != "Linux":
            return

        while True:
            for i in range(5):
                try:
                    # Print the values to the serial port
                    temperature_c = self._dht_device.temperature
                    humidity = self._dht_device.humidity
                    self._data_store.store_in_db(temperature_c, humidity)
                    break

                except RuntimeError as error:
                    # Errors happen fairly often, DHT's are hard to read, just keep going
                    print(error.args[0])
                    sleep(2.0)
                    continue
                except Exception as error:
                    self._dht_device.exit()
                    raise error
            sleep(60 * 5)

