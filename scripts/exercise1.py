import rospy
from geometry_msgs.msg import Twist

def publisher():
    pub = rospy.Publisher('mobile_base/commands/velocity', Twist, queue_size=0)
    rospy.init_node('Walker', anonymous=True)
    rate = rospy.Rate(10) #10hz

    desired_velocity = Twist()
    desired_velocity.angular.z = 2 # Rota with 2 m/sec.
    desired_velocity.linear.x = 0.2 # Forward with 0.2 m/sec.

    while not rospy.is_shutdown():
        pub.publish(desired_velocity)
        rate.sleep()


if __name__ == "__main__":
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
