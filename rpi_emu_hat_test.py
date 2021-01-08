from sense_emu import SenseHat
import time

sense = SenseHat()
sense.clear


while True:
    temperature = sense.get_temperature()
    humidity = sense.get_humidity()
    pressure = sense.get_pressure()
    print("temperature " temperature)
    print("humidity " humidity)
    print("pressure " pressure)  
    
    time.sleep(5)
