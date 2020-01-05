#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from std_msgs.msg import Int32
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
LeftWheel = RpiMotorLib.A4988Nema(leftDirection, leftStep, leftMs13, "DRV8825") 


def callback(data):
	rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

def listener():
	rospy.init_node('listener', anonymous=True)
	
	rospy.Subscriber("left", Int32, runRightWheel)
	rospy.Subscriber("right", Int32, runLeftWheel)
	
	rospy.spin()


def runLeftWheel(stepNumber, dir=True, stepDelay=0.0005):
# sends signals to the left motor driver...
	# call the function, pass the arguments
	#RightWheel.motor_go(dir, "1/16" , stepNumber, stepDelay, False, .05)	 	# direction: False CC True CCC, number of steps, step delay, verbose output, init delay
	#steps = int(stepNumber)
	#print("Type of StepNumber: ", type(steps))
	#stepNumber = int(stepNumber)
	print("Im here")
	LeftWheel.motor_go(dir, "1/16" , 20000, stepDelay, False, .05)                     # direction: False CC True CCC, number of steps, step delay, verbose output, init delay


def runRightWheel(stepNumber, dir=False, stepDelay=0.0005):
#sends signals to the right motor driver...
	# call the function, pass the arguments
	#steps = int(stepNumber)
	#print("Type of StepNumber: ", type(steps))
	#stepNumber = int(stepNumber)
	print("Im here")
	RightWheel.motor_go(dir, "1/16" , 20000, stepDelay, False, .05)			# direction: False CC True CCC, number of steps, step delay, verbose output, init delay

def main():
	#runWheel(False,2000,0.0005);
	#runLeftWheel(True,2000,0.0005);
	listener()
    
# ===== Programmstart =====       
if __name__ == "__main__":
    main()


# good practise to cleanup GPIO at some point before exit
GPIO.cleanup()
