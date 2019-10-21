import rospy
import RPi.GPIO as GPIO #cannot import here as we are not on the raspberry - this node needs to run on the raspberry i guess
from time import sleep
from std_msgs.msg import Float64

SERVO_PIN = 21
FREQ = 90 #dont forget

GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)

p = GPIO.PWM(SERVO_PIN, FREQ)
p.start(2.5)

# TODO: find out to which sensitivity e.g. dutycycle of 12.22224345236234 it makes a differnece

def callback(data):
	p.ChangeDutyCycle(float(data.data)) 
	rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)
	    
def listener():

	 # In ROS, nodes are uniquely named. If two nodes with the same
	    # name are launched, the previous one is kicked off. The
	    # anonymous=True flag means that rospy will choose a unique
	    # name for our 'listener' node so that multiple listeners can
	    # run simultaneously.
	rospy.init_node('listener', anonymous=True)

	rospy.Subscriber('steering', Float64, callback)

	    # spin() simply keeps python from exiting until this node is stopped
	rospy.spin()
	    # does cleanining up the GPIOs here work?
	    # GPIO.cleanup()


if __name__ == '__main__':
	listener()

	# TODO: google how to cleanup after deinit?
