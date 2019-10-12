#!/usr/bin/env python3
from ev3dev2.sound import Sound
from ev3dev2.sensor.lego import InfraredSensor
from time import sleep

# Infrared remote
remote = InfraredSensor()
remote.mode = remote.MODE_IR_REMOTE

sound = Sound()
#play a standard beep
sound.beep()

while True:
        # Read remote
        button_code = remote.value()

        # Move robot in response to infrared remote
        if button_code == remote.TOP_LEFT_TOP_RIGHT:
            sound.speak('Right')
        if button_code == remote.TOP_LEFT_TOP_RIGHT:
            sound.speak('Left')