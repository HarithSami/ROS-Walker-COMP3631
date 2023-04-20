import rospy
from geometry_msgs.msg import Twist

def publisher():
    pub = rospy.Publisher('mobile_base/commands/velocity', Twist, queue_size=0)
    rospy.init_node('Walker', anonymous=True)
    rate = rospy.Rate(10) #10hz

    desired_velocity = Twist()

    while not rospy.is_shutdown():
        for _ in range (30):
            
            desired_velocity.linear.x = 0.2 # Forward with 0.2 m/sec.
            desired_velocity.angular.z = 0 # Rotating with 2 m/sec.
            pub.publish(desired_velocity)
            rate.sleep()
        for _ in range (10):
            desired_velocity.linear.x = 0 # Forward with 0.2 m/sec.
            desired_velocity.angular.z = 1.5708 # Rotating with 2 m/sec.
            pub.publish(desired_velocity)
            rate.sleep()
            
            

if __name__ == "__main__":
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
