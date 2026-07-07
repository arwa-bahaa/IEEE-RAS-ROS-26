## Project Structure

Task_14/
│
├── launch/
│   └── gazebo_autonomous.launch.py
│
├── worlds/
│   └── my_world.world
│
├── task_14/
│   ├── __init__.py
│   └── autonomous_mover.py
│
├── package.xml
├── setup.py
└── README.md


## Build
cd ~/ros2_ws

colcon build --packages-select task_14

source install/setup.bash


## Run
export TURTLEBOT3_MODEL=burger

ros2 launch task_14 gazebo_autonomous.launch.py


## Autonomous Behavior
The robot publishes velocity commands to the `/cmd_vel` topic.
Movement sequence:

1. Move forward.
2. Rotate left.
3. Move forward.
4. Rotate right.
5. Repeat continuously.

## ROS 2 Nodes
/autonomous_mover
/robot_state_publisher


## Topics
Published:
/cmd_vel

