# ROS Beginner Exercises

This beginner ROS project contains four Python scripts designed to provide a hands-on introduction to ROS and mobile robot control. Each script demonstrates different robot movement behaviors using the `geometry_msgs/Twist` message.

## Getting Started

Clone the repository into your catkin workspace's `src` directory:

cd ~/catkin_ws/src
git clone https://github.com/yourusername/ros_beginner_exercises.git

Build the package using catkin:

cd ~/catkin_ws
catkin_make

## Exercises

1. **Firstwalk.py**: A simple forward and backward movement.
2. **Excersice1.py**: A combination of linear and angular movement.
3. **Exercise2.py**: A sequence of forward movement and turning.
4. **Exercise3.py**: Similar to Exercise 2, but with bumper collision detection.

To run any of the exercises, use the following command:

rosrun ros_beginner_exercises <exercise_name>.py

Replace `<exercise_name>` with the name of the exercise you want to run (e.g., `firstwalk`, `exercise1`, etc.).

## Dependencies

This project requires the following ROS packages:

- rospy
- geometry_msgs
- kobuki_msgs (for Exercise 3)

Make sure to install these packages using `rosdep` or `apt-get` if you haven't already.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

## Contributing

To contribute to this project, please submit a pull request or open an issue on the GitHub repository.
