#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from std_msgs.msg import Int32
from geometry_msgs.msg import Twist
import RPi.GPIO as GPIO

# import the library
from RpiMotorLib import RpiMotorLib
    

# define GPIO pins right wheel
rightMs13 = (16, 20, 21) 	# Microstep Resolution MS1-MS3 -> GPIO Pin
rightDirection= 26       	# Direction -> GPIO Pin
rightStep = 19      		# Step -> GPIO Pin

# define GPIO pins left wheel
leftMs13 = (2, 3, 4) 		# Microstep Resolution MS1-MS3 -> GPIO Pin
leftDirection= 27       	# Direction -> GPIO Pin
leftStep = 17      		# Step -> GPIO Pin

activateSteppers = 23
activateLED = 22
GPIO.setmode(GPIO.BCM)
GPIO.setup(activateSteppers,GPIO.OUT)
GPIO.setup(activateLED,GPIO.OUT)

# Declare a instance of class pass GPIO pins numbers and the motor type of the right and left wheel
RightWheel = RpiMotorLib.A4988Nema(rightDirection, rightStep, rightMs13, "DRV8825") 
LeftWheel = RpiMotorLib.A4988Nema(leftDirection, leftStep, leftMs13, "DRV8825") 


def callback(data):
	rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

def listener():
	rospy.init_node('listener', anonymous=True)
	
	rospy.Subscriber("robCommandLeft", Twist, runRightWheel)
	rospy.Subscriber("robCommandRight", Twist, runLeftWheel)
	
	rospy.spin()


def runLeftWheel(data):
# sends signals to the left motor driver...
	# call the function, pass the arguments
	#RightWheel.motor_go(dir, "1/16" , stepNumber, stepDelay, False, .05)	 	# direction: False CC True CCC, number of steps, step delay, verbose output, init delay
	#steps = int(stepNumber)
	#print("Type of StepNumber: ", type(steps))
	#stepNumber = int(stepNumber)
	print("left command: ", type(data.linear.x))
	stepNumber = int(data.angular.z)
	if (int(data.linear.y) == 1):
	    dir = True
	else:
	    dir = False
	steps = data.linear.x
	print("stepsLeft: ", data.linear,x)
	LeftWheel.motor_go(dir, "1/16" , stepNumber, steps, False, .05)                     # direction: False CC True CCC, number of steps, step delay, verbose output, init delay


def runRightWheel(data):
#sends signals to the right motor driver...
	# call the function, pass the arguments
	#steps = int(stepNumber)
	#print("Type of StepNumber: ", type(steps))
	stepNumber = int(data.angular.z)
	print("right command: ", type(data.linear.x))
	if (int(data.linear.y) == 1):
	    dir = True
	else:
	    dir = False
	steps = data.linear.x
	print("stepsRight: ", steps)
	RightWheel.motor_go(dir, "1/16" , stepNumber, steps, False, .05)			# direction: False CC True CCC, number of steps, step delay, verbose output, init delay

def main():
	#runWheel(False,2000,0.0005);
	#runLeftWheel(True,2000,0.0005

	listener() 

    
# ===== Programmstart =====       
if __name__ == "__main__":
    GPIO.output(activateSteppers, GPIO.HIGH)
    GPIO.output(activateLED, GPIO.HIGH) 
    main()


# good practise to cleanup GPIO at some point before exit
GPIO.cleanup()
