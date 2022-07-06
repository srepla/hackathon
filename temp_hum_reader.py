import time
import board
import adafruit_dht


class TempHumReader:

    @staticmethod
    def read():
        dhtDevice = adafruit_dht.DHT22(board.D4)

        for i in range(5):
            try:
                # Print the values to the serial port
                temperature_c = dhtDevice.temperature
                humidity = dhtDevice.humidity
                print("Temp: {:.1f} C    Humidity: {}% ".format(temperature_c, humidity))
                return temperature_c, humidity

            except RuntimeError as error:
                # Errors happen fairly often, DHT's are hard to read, just keep going
                print(error.args[0])
                time.sleep(2.0)
                continue
            except Exception as error:
                dhtDevice.exit()
                raise error
