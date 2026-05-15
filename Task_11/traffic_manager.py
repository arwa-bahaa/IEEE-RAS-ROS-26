import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Pose2D
from std_msgs.msg import Int32

import math


class TrafficManager(Node):

    def __init__(self):
        super().__init__('traffic_manager')

        self.safety_zone = 6.0

        self.my_x = 5.0
        self.my_y = 5.0
        self.my_priority = 2

        self.other_pos = None
        self.other_priority = None

        self.create_subscription(Pose2D, 'robot/position', self.pos_callback, 10)
        self.create_subscription(Int32, 'robot/priority', self.pri_callback, 10)

        self.timer = self.create_timer(0.2, self.check)

        self.get_logger().info("Traffic Manager Started")

    def pos_callback(self, msg):
        self.other_pos = msg
        self.get_logger().info(f"POS ({msg.x:.2f}, {msg.y:.2f})")

    def pri_callback(self, msg):
        self.other_priority = msg.data
        self.get_logger().info(f"PRI {msg.data}")

    def check(self):

        if self.other_pos is None or self.other_priority is None:
            self.get_logger().warn("Waiting for data")
            return

        dx = self.my_x - self.other_pos.x
        dy = self.my_y - self.other_pos.y

        distance = math.sqrt(dx * dx + dy * dy)

        if distance < self.safety_zone and self.other_priority > self.my_priority:
            self.get_logger().warn(
                f"DANGER Distance={distance:.2f} Priority={self.other_priority}"
            )
        else:
            self.get_logger().info(
                f"CLEAR Distance={distance:.2f}"
            )


def main():
    rclpy.init()
    node = TrafficManager()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
