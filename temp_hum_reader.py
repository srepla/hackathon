import time
import board
import adafruit_dht


class TempHumReader:

    def __init__(self):
        self._dht_device = adafruit_dht.DHT22(board.D4)

    def read(self):
        for i in range(5):
            try:
                # Print the values to the serial port
                temperature_c = self._dht_device.temperature
                humidity = self._dht_device.humidity
                print("Temp: {:.1f} C    Humidity: {}% ".format(temperature_c, humidity))
                return temperature_c, humidity

            except RuntimeError as error:
                # Errors happen fairly often, DHT's are hard to read, just keep going
                print(error.args[0])
                time.sleep(2.0)
                continue
            except Exception as error:
                self._dht_device.exit()
                raise error
