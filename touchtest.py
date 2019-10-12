#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, MoveSteering, OUTPUT_A, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds

ts = TouchSensor()
leds = Leds()
lm = LargeMotor(OUTPUT_B)
rm = LargeMotor(OUTPUT_C)
steer_pair = MoveSteering(OUTPUT_B, OUTPUT_C)

while True:
    if ts.is_pressed:
        steer_pair.on_for_seconds(steering=100, speed=100, seconds=1)
