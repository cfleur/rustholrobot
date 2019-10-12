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
        sleep(0.3)
        sound.speak('Begin')
        cache = True

while cache == True:
    tank_pair.on_for_seconds(100, 100, 1.9)
    sleep(2)
    # turn 1 left
    tank_pair.on_for_seconds(100, -100, 0.85)
    sleep(0.9)
    tank_pair.on_for_seconds(100, 100, 1.3)
    sleep(1.4)
    # turn 2 left
    tank_pair.on_for_seconds(100, -100, 0.85)
    sleep(0.9)
    tank_pair.on_for_seconds(100, 100, 1.3)
    sleep(1.4)
    # turn 3 right
    tank_pair.on_for_seconds(-100, 100, 0.85)
    sleep(0.9)
    tank_pair.on_for_seconds(100, 100, 2.8)
    sleep(2.9)
    # turn 4 right
    tank_pair.on_for_seconds(-100, 100, 0.85)
    sleep(0.9)
    tank_pair.on_for_seconds(100, 100, 1.3)
    sleep(1.4)
    # turn 5 half-right
    tank_pair.on_for_seconds(-100, 100, 0.42)
    sleep(0.5)
    tank_pair.on_for_seconds(100, 100, 1.4)
    sleep(1.5)
    # turn 6 half-right
    tank_pair.on_for_seconds(-100, 100, 0.42)
    sleep(0.5)
    tank_pair.on_for_seconds(100, 100, 1.7)
    sleep(1.8)
    # turn 7 full-right
    tank_pair.on_for_seconds(-100, 100, 1.7)
    sleep(1.8)
    tank_pair.on_for_seconds(100, 100, 0.8)
    sleep(0.9)
    # turn 8 right
    tank_pair.on_for_seconds(-100, 100, 0.85)
    sleep(0.9)
    tank_pair.on_for_seconds(100, 100, 0.8)
    sleep(0.9)
    # turn 9 left
    tank_pair.on_for_seconds(100, -100, 0.85)
    sleep(0.9)
    tank_pair.on_for_seconds(100, 100, 1.5)
    sleep(1.6)
    # turn 10 right
    tank_pair.on_for_seconds(-100, 100, 0.85)
    sleep(0.9)
    tank_pair.on_for_seconds(100, 100, 2.5)
    sleep(2.6)
    # turn 11 right
    tank_pair.on_for_seconds(-100, 100, 0.85)
    sleep(0.9)
    tank_pair.on_for_seconds(100, 100, 4.2)
    sleep(4.3)
    # turn 12 left
    tank_pair.on_for_seconds(100, -100, 0.85)
    sleep(0.9)
    tank_pair.on_for_seconds(100, 100, 0.9)
    sleep(1)
    tank_pair.off()
    sound.beep()
    sleep(0.3)
    sound.speak('End')
    sound.beep()
    sleep(0.2)
    sound.beep()
    cache = False