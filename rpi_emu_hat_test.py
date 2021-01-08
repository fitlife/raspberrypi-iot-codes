from sense_emu import SenseHat
import time

sense = SenseHat()
sense.clear


while True:
    temperature = sense.get_temperature()
    humidity = sense.get_humidity()
    pressure = sense.get_pressure()
    print(temperature)
    print("temperature")
    print()
    print(humidity)
    print("humidity")
    print()
    print(pressure)
    print("pressure")
    print()
    print("................................")
    time.sleep(5)
