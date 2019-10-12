#!/usr/bin/env python3
from ev3dev2.motor import MediumMotor, MoveSteering, OUTPUT_A, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank
from ev3dev2.sound import Sound
from ev3dev2.sensor.lego import InfraredSensor
from time import sleep

mm = MediumMotor('outA');  # "arm" 

# Infrared remot
ir = InfraredSensor()
ir.mode = ir.MODE_IR_REMOTE

sound = Sound()
# Play a standard beep on boot up
sound.beep()

while True:
    button_code = ir.value()
    if button_code == ir.TOP_LEFT:
        mm.run_timed(time_sp=5, speed_sp=1000)
    if button_code == ir.BOTTOM_LEFT:
        mm.run_timed(time_sp=5, speed_sp=-1000)
    else:
        mm.off()
