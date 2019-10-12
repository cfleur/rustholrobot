#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, MoveSteering, OUTPUT_A, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank
from ev3dev2.sound import Sound
from ev3dev2.sensor.lego import InfraredSensor
from time import sleep

# Boolean for Cache script
cache = False

# Tank pair
tank_pair = MoveTank(OUTPUT_B, OUTPUT_C)

# Infrared remot
ir = InfraredSensor()
ir.mode = ir.MODE_IR_REMOTE

sound = Sound()
# Play a standard beep on boot up
sound.beep()

while cache == False:
    button_code = ir.value()
    if button_code == ir.TOP_LEFT:
        tank_pair.on(left_speed=100, right_speed=100)
    elif button_code == ir.TOP_LEFT_BOTTOM_LEFT:
        tank_pair.on(left_speed=100, right_speed=0)
    elif button_code == ir.TOP_LEFT_TOP_RIGHT:
        tank_pair.on(left_speed=0, right_speed=100)
    elif button_code == ir.TOP_RIGHT:
        tank_pair.on(left_speed=-100, right_speed=100)
    elif button_code == ir.BOTTOM_RIGHT:
        tank_pair.on(left_speed=-100, right_speed=-100)
    elif button_code == ir.BOTTOM_LEFT:
        tank_pair.on(left_speed=100, right_speed=-100)
    elif button_code == ir.BOTTOM_LEFT_BOTTOM_RIGHT:
        tank_pair.on(left_speed=0, right_speed=-100)
    elif button_code == ir.TOP_RIGHT_BOTTOM_RIGHT:
        tank_pair.on(left_speed=-100, right_speed=0)
    elif button_code == ir.TOP_LEFT_BOTTOM_RIGHT:
        sound.tone([(500, 1000, 400)] * 3)
    else:
        tank_pair.off()
    sleep(0.01)
    if ir.top_left(channel=3) == True:
        sound.beep()
        cache = True

while cache == True:
    tank_pair.on_for_seconds(100, 100, 3)
    tank_pair.on_for_seconds(-100, 100, 1)
    tank_pair.on_for_seconds(100, 100, 3)
    cache == False