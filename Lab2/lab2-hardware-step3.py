## This program will make use of a thermometer emulator
import time
import string

from thermometer_emu import thermo

t = thermo(15)

while True:
    t.update()
    print("The current temperature is: ", t.temp)
    time.sleep(5)
