# Add your Python code here. E.g.
#Created by; Mariam Abugamga
#Date; oct, 2, 2020
#this program uses neopixels to make a traffic light

from microbit import *
import neopixel


neopixels_variable = neopixel.NeoPixel(pin16, 4)
neopixels_variable[0] = (0, 0, 0)
neopixels_variable[1] = (0, 0, 0)
neopixels_variable[2] = (0, 0, 0)
neopixels_variable[3] = (0, 0, 0)
neopixels_variable.show()

while True:
    # turn on green light
    neopixels_variable[2] = (0, 255, 0)
    neopixels_variable.show()
    sleep(1000)
    # turn green light off
    neopixels_variable[0] = (0, 0, 0)
    neopixels_variable[1] = (0, 0, 0)
    neopixels_variable[2] = (0, 0, 0)
    neopixels_variable[3] = (0, 0, 0)
    neopixels_variable.show()
    # turn on yellow light
    neopixels_variable[1] = (255, 255, 0)
    neopixels_variable.show()
    sleep(1000)
    #turn yellow light off
    neopixels_variable[0] = (0, 0, 0)
    neopixels_variable[1] = (0, 0, 0)
    neopixels_variable[2] = (0, 0, 0)
    neopixels_variable[3] = (0, 0, 0)
    #turn on red light
    neopixels_variable[0]= (255, 0, 0)
    neopixels_variable.show()
    sleep(1000)
    #turn red light off
    neopixels_variable[0] = (0, 0, 0)
    neopixels_variable[1] = (0, 0, 0)
    neopixels_variable[2] = (0, 0, 0)
    neopixels_variable[3] = (0, 0, 0)
