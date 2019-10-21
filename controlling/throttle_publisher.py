import rospy
from std_msgs.msg import Float64

def control():
    pub = rospy.Publisher('throttle', Float64, queue_size=10)
    rospy.init_node('control', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    
    try: 
        while not rospy.is_shutdown():
            dutycycle = input("dutycycle: ")
            hello_str = "hello world %s" % rospy.get_time()
            rospy.loginfo(dutycycle)
            pub.publish(float(dutycycle))
            rate.sleep()
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    try:
        control()
    except rospy.ROSInterruptException:
        pass

