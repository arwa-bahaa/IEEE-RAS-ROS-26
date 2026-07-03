import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Pose2D
from std_msgs.msg import Int32

import math


class TrafficManager(Node):

    def __init__(self):
        super().__init__('traffic_manager')

        # Parameters
        self.declare_parameter('safety_zone', 2.0)
        self.declare_parameter('my_x', 5.0)
        self.declare_parameter('my_y', 5.0)
        self.declare_parameter('my_priority', 2)

        self.safety_zone = self.get_parameter(
            'safety_zone').get_parameter_value().double_value

        self.my_x = self.get_parameter(
            'my_x').get_parameter_value().double_value

        self.my_y = self.get_parameter(
            'my_y').get_parameter_value().double_value

        self.my_priority = self.get_parameter(
            'my_priority').get_parameter_value().integer_value

        self.robot_position = None
        self.robot_priority = None

        
        self.create_subscription(
            Pose2D,
            'robot/position',
            self.position_callback,
            10
        )

        self.create_subscription(
            Int32,
            'robot/priority',
            self.priority_callback,
            10
        )

        
        self.timer = self.create_timer(0.2, self.check_robot)

        self.get_logger().info("Traffic Manager Started")

    def position_callback(self, msg):
        self.robot_position = msg

    def priority_callback(self, msg):
        self.robot_priority = msg.data

    def check_robot(self):

        if self.robot_position is None or self.robot_priority is None:
            self.get_logger().warn("Waiting for robot data...")
            return

        dx = self.my_x - self.robot_position.x
        dy = self.my_y - self.robot_position.y

        distance = math.sqrt(dx * dx + dy * dy)

        if distance <= self.safety_zone and self.robot_priority > self.my_priority:

            self.get_logger().warn(
                f"DANGER | Distance = {distance:.2f} m | "
                f"Other Priority = {self.robot_priority}"
            )

        else:

            self.get_logger().info(
                f"CLEAR | Distance = {distance:.2f} m"
            )


def main():

    rclpy.init()

    node = TrafficManager()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
    
