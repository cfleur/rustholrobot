#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, MoveSteering, OUTPUT_A, OUTPUT_B, OUTPUT_C, SpeedDPS, MoveTank
from ev3dev2.sound import Sound
from time import sleep

# Tank pair
tank_pair = MoveTank(OUTPUT_B, OUTPUT_C)

sound = Sound()
# Play a standard beep on boot up
sound.beep()

with open('motor.log', 'r') as f:
    for line in f:
        speeds = str.split(line, ',')
        lm = int(speeds[0]) 
        rm = int(speeds[1])
        tank_pair.on(left_speed=SpeedDPS(lm), right_speed=SpeedDPS(rm))
        sleep(0.01)
