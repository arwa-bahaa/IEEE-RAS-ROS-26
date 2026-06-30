This project implements a decentralized communication system between multiple robots using ROS2.  
Each robot broadcasts its status, and a traffic manager node processes this data to ensure safe navigation.
The system simulates real-time robotic interaction in a warehouse environment.


1. Fleet Emulator Node
- Simulates a robot in a fleet
- Publishes two types of data:
- Position (x, y) using `geometry_msgs/msg/Pose2D`
- Priority using `std_msgs/msg/Int32`
- Publishes at 10 Hz frequency

2. Traffic Manager Node
- Subscribes to robot data
- Processes incoming position and priority
- Computes distance between robots
- Makes a decision:
- CLEAR: Safe distance
- DANGER: Collision risk + higher priority robot nearby


Yielding Logic:
The decision is based on the following rule:
- Compute distance:
      distance = sqrt((x1 - x2)^2 + (y1 - y2)^2)

Safety Rule:
A DANGER state is triggered when:
Distance is less than 2.0 meters (Safety Zone)
AND the other robot has higher priority than my robot
Otherwise the state is CLEAR

  Then:
  - Output: DANGER

  Else:
  - Output: CLEAR
 System Output Examples:
 CLEAR:
 [CLEAR] robot2 | dist=3.45 | p=2

 DANGER:
 [DANGER] robot1 | dist=1.20 | p=5 > my_p=2 → YIELD


The system handles two separate data streams:
- Position data
- Priority data

Synchronization is achieved by:
- Storing the latest received values in class variables
- Running a periodic timer to combine both values
- Ensuring both values exist before making a decision
