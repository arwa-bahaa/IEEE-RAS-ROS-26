The exact command you used to draw your "Manual Star:
for i in {1..5}; do   ros2 topic pub --once /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0}, angular: {z: 0.0}}";   sleep 1;   ros2 topic pub --once /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 0.0}, angular: {z: -2.5}}";   sleep 1; done


Nodes:
Nodes are programs that run in ROS 2. Each node does one job, like moving the turtle or reading the keyboard.

Topics:
They are used to send and receive data between nodes, like turtle movement and position.

Services:
They are used for requests and responses, like resetting or spawning the turtle.
