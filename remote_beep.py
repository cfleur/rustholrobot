#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, MoveSteering, OUTPUT_A, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank
from ev3dev2.sound import Sound
from ev3dev2.sensor.lego import InfraredSensor
from time import sleep

# Tank pair
tank_pair = MoveTank(OUTPUT_B, OUTPUT_C)
lm = LargeMotor('outB');  # assert lm.connected  # left motor
rm = LargeMotor('outC');  # assert rm.connected  # right motor

# Infrared remot
ir = InfraredSensor()
ir.mode = ir.MODE_IR_REMOTE

sound = Sound()
# Play a standard beep on boot up
sound.beep()

while True:
    lm_sp = lm.speed_sp
    rm_sp = rm.speed_sp
    print("lm: ", lm_sp, "rm: ", rm_sp)
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
