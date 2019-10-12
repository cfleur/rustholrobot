#!/usr/bin/env python3
from ev3dev2.sound import Sound
from ev3dev2.sensor.lego import InfraredSensor
from time import sleep

# Infrared remote
ir = InfraredSensor()

sound = Sound()
#play a standard beep
sound.beep()

def top_left_channel_1_action(state):
    print("top left on channel 1: %s" % state)

def bottom_right_channel_1_action(state):
    print("bottom right on channel 1: %s" % state)

ir = InfraredSensor()
ir.on_channel1_top_left = top_left_channel_1_action
ir.on_channel1_bottom_right = bottom_right_channel_1_action

while True:
    ir.process()
    time.sleep(0.01)