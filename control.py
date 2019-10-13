#!/usr/bin/env python3
from ev3dev2.motor import MediumMotor, LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank
from ev3dev2.sound import Sound
from ev3dev2.sensor.lego import InfraredSensor
from time import sleep


# Grabber arm
mm = MediumMotor('outA')

# Tank pair
tank_pair = MoveTank(OUTPUT_B, OUTPUT_C)

# Infrared remot
ir = InfraredSensor()
ir.mode = ir.MODE_IR_REMOTE

sound = Sound()
# Play a standard beep on boot up
sound.beep()

while True:
    button_code = ir.value()
    #Forward
    if ir.top_left(channel=1) == True and ir.top_right(channel=4) == True:
        tank_pair.on(left_speed=100, right_speed=100)
    #Backward
    elif ir.bottom_left(channel=1) == True and ir.bottom_right(channel=4) == True:
        tank_pair.on(left_speed=-100, right_speed=-100)
    elif ir.top_left(channel=1) == True and ir.bottom_right(channel=4) == True:
        tank_pair.on(left_speed=100, right_speed=-100)
    elif ir.top_right(channel=4) == True and ir.bottom_left(channel=1) == True:
        tank_pair.on(left_speed=-100, right_speed=100)
    elif ir.top_left(channel=1) == True:
        tank_pair.on(left_speed=100, right_speed=0)
    elif ir.bottom_left(channel=1) == True:
        tank_pair.on(left_speed=-100, right_speed=0)
    elif ir.top_right(channel=4) == True:
        tank_pair.on(left_speed=0, right_speed=100)
    elif ir.bottom_right(channel=4) == True:
        tank_pair.on(left_speed=0, right_speed=-100)
    elif ir.bottom_right(channel=1) == True:
        tank_pair.on(left_speed=-100, right_speed=-100)
    elif ir.bottom_left(channel=1) == True:
        tank_pair.on(left_speed=100, right_speed=-100)
    elif ir.top_left(channel=4) == True:
        mm.run_timed(time_sp=5, speed_sp=1000)
    elif ir.bottom_left(channel=4) == True:
        mm.run_timed(time_sp=5, speed_sp=-1000)
    else:
        tank_pair.off()
    sleep(0.01)