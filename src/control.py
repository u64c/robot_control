#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import RPi.GPIO as GPIO

# import the library
from RpiMotorLib import RpiMotorLib
    

# define GPIO pins right wheel
rightMs13 = (16, 20, 21) 	# Microstep Resolution MS1-MS3 -> GPIO Pin
rightDirection= 26       	# Direction -> GPIO Pin
rightStep = 19      		# Step -> GPIO Pin

# define GPIO pins left wheel
leftMs13 = (2, 3, 4) 	# Microstep Resolution MS1-MS3 -> GPIO Pin
leftDirection= 27       	# Direction -> GPIO Pin
leftStep = 17      			# Step -> GPIO Pin

# Declare a instance of class pass GPIO pins numbers and the motor type of the right and left wheel
RightWheel = RpiMotorLib.A4988Nema(rightDirection, rightStep, rightMs13, "DRV8825") 



def runLeftWheel(dir,stepNumber,stepDelay):
"""
sends signals to the left motor driver...
"""
	# call the function, pass the arguments
	RightWheel.motor_go(dir, "1/16" , stepNumber, stepDelay, False, .05)	 	# direction: False CC True CCC, number of steps, step delay, verbose output, init delay


def runRightWheel(dir,stepNumber,stepDelay):
"""
sends signals to the right motor driver...
"""
	# call the function, pass the arguments
	LeftWheel.motor_go(dir, "1/16" , stepNumber, stepDelay, False, .05)			# direction: False CC True CCC, number of steps, step delay, verbose output, init delay

def main():
	runLeftWheel(False,20000,0.005);
	runRightWheel(True,20000,0.005);

    
# ===== Programmstart =====       
if __name__ == "__main__":
    main()


# good practise to cleanup GPIO at some point before exit
GPIO.cleanup()
