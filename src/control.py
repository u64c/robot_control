#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import RPi.GPIO as GPIO


# import the library
from RpiMotorLib import RpiMotorLib
    
#define GPIO pins
GPIO_pins = (16, 20, 21) # Microstep Resolution MS1-MS3 -> GPIO Pin
direction= 26       # Direction -> GPIO Pin
step = 19      # Step -> GPIO Pin


# Declare a instance of class pass GPIO pins numbers and the motor type
mymotortest = RpiMotorLib.A4988Nema(direction, step, GPIO_pins, "DRV8825")


# call the function, pass the arguments
mymotortest.motor_go(False, "1/16" , 20000, .00005, False, .05)

# good practise to cleanup GPIO at some point before exit
GPIO.cleanup()
