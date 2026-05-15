import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Pose2D
from std_msgs.msg import Int32

import random


class FleetEmulator(Node):

    def __init__(self):
        super().__init__('fleet_emulator')

        self.pos_pub = self.create_publisher(Pose2D, 'robot/position', 10)
        self.pri_pub = self.create_publisher(Int32, 'robot/priority', 10)

        self.timer = self.create_timer(0.1, self.publish_data)

        self.x = random.uniform(4.0, 6.0)
        self.y = random.uniform(4.0, 6.0)

        self.priority = random.randint(3, 5)

        self.get_logger().info("Fleet Emulator Started")

    def publish_data(self):

        self.x += random.uniform(-0.5, 0.5)
        self.y += random.uniform(-0.5, 0.5)

        pos = Pose2D()
        pos.x = self.x
        pos.y = self.y
        pos.theta = 0.0

        pri = Int32()
        pri.data = self.priority

        self.pos_pub.publish(pos)
        self.pri_pub.publish(pri)

        self.get_logger().info(
            f"POS ({self.x:.2f}, {self.y:.2f}) PRI {self.priority}"
        )


def main():
    rclpy.init()
    node = FleetEmulator()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
