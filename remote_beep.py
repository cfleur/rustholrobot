#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, MoveSteering, OUTPUT_A, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank
from ev3dev2.sound import Sound
from ev3dev2.sensor.lego import InfraredSensor
from time import sleep

# Steer pair

lm = LargeMotor(OUTPUT_B)
rm = LargeMotor(OUTPUT_C)
steer_pair = MoveSteering(OUTPUT_B, OUTPUT_C)

# Infrared remote
ir = InfraredSensor()

sound = Sound()
# Play a standard beep on boot up
sound.beep()

def top_left_channel_1_action():
    steer_pair.on_for_seconds(steering=0, speed=50, seconds=1)

def top_right_channel_1_action():
    steer_pair.on_for_seconds(steering=100, speed=50, seconds=1)

def bottom_right_channel_1_action():
    steer_pair.on_for_seconds(steering=0, speed=-50, seconds=1)

def bottom_left_channel_1_action():
    steer_pair.on_for_seconds(steering=-100, speed=50, seconds=1)

    
ir.on_channel1_top_right = top_right_channel_1_action
ir.on_channel1_top_left = top_left_channel_1_action
ir.on_channel1_bottom_right = bottom_right_channel_1_action
ir.on_channel1_bottom_left = bottom_left_channel_1_action

while True:
    button_code = ir.value()
    if button_code == ir.TOP_LEFT:
        steer_pair.on(75, 75)
    elif button_code == ir.TOP_RIGHT:
        steer_pair.on(-75, 75)
    elif button_code == ir.BOTTOM_RIGHT:
        steer_pair.on(-75,-75)
    elif button_code == ir.BOTTOM_LEFT:
        steer_pair.on(75, -75)
    else:
        steer_pair.off(brake=True)