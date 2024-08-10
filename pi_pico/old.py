from machine import ADC, Pin
import time

sensor1 = ADC(Pin(26))
sensor2 = ADC(Pin(27)) 
sensor3 = ADC(Pin(28)) 

while True:
    value1 = sensor1.read_u16()
    value2 = sensor2.read_u16()
    value3 = sensor3.read_u16()

    print("Sensor 1: ", value1)
    print("Sensor 2: ", value2)
    print("Sensor 3: ", value3)


    time.sleep(1)

