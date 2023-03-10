from engi1020.arduino.api import*
from time import *

while True:
    # Recieve data from light and temp sensor
    light = analog_read(6)
    temp = analog_read(3)
    # Compares data with danger threshold
    if light >= 750 or temp >= 750:
        # Sets Light and sound alarm on
        digital_write(4,True)
        analog_write(5,216)
        # If button Pressed Both sound and light alarm shut off
        if digital_read(6):
            digital_write(4, False)
            digital_write(5,False)
            sleep(100)