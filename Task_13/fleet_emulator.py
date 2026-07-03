import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Pose2D
from std_msgs.msg import Int32

import random

class FleetEmulator(Node):

    def __init__(self):
        super().__init__('fleet_emulator')

        self.pos_pub1 = self.create_publisher(Pose2D, 'robot1/position', 10)
        self.pri_pub1 = self.create_publisher(Int32, 'robot1/priority', 10)

        self.pos_pub2 = self.create_publisher(Pose2D, 'robot2/position', 10)
        self.pri_pub2 = self.create_publisher(Int32, 'robot2/priority', 10)

        self.pos_pub3 = self.create_publisher(Pose2D, 'robot3/position', 10)
        self.pri_pub3 = self.create_publisher(Int32, 'robot3/priority', 10)

        self.timer = self.create_timer(0.1, self.publish_data)

        self.x1 = random.uniform(4.5, 5.5)
        self.y1 = random.uniform(4.5, 5.5)

        self.x2 = random.uniform(3.5, 6.5)
        self.y2 = random.uniform(3.5, 6.5)

        self.x3 = random.uniform(4.0, 6.0)
        self.y3 = random.uniform(4.0, 6.0)

        self.get_logger().info("Fleet Emulator Started")

    def publish_data(self):

        self.x1 += random.uniform(-0.4, 0.4)
        self.y1 += random.uniform(-0.4, 0.4)

        self.x2 += random.uniform(-0.5, 0.5)
        self.y2 += random.uniform(-0.5, 0.5)

        self.x3 += random.uniform(-0.4, 0.4)
        self.y3 += random.uniform(-0.4, 0.4)

        if self.x1 < 5:
            self.x1 += 0.1
        else:
            self.x1 -= 0.1

        if self.y1 < 5:
            self.y1 += 0.1
        else:
            self.y1 -= 0.1

        if self.x2 < 5:
            self.x2 += 0.05
        else:
            self.x2 -= 0.05

        if self.y2 < 5:
            self.y2 += 0.05
        else:
            self.y2 -= 0.05

        if self.x3 < 5:
            self.x3 += 0.08
        else:
            self.x3 -= 0.08

        if self.y3 < 5:
            self.y3 += 0.08
        else:
            self.y3 -= 0.08

        p1 = random.randint(1, 5)
        p2 = random.randint(1, 5)
        p3 = random.randint(1, 5)
      
        pos1 = Pose2D()
        pos1.x = self.x1
        pos1.y = self.y1
        pos1.theta = 0.0

        pri1 = Int32()
        pri1.data = p1

        self.pos_pub1.publish(pos1)
        self.pri_pub1.publish(pri1)

        pos2 = Pose2D()
        pos2.x = self.x2
        pos2.y = self.y2
        pos2.theta = 0.0

        pri2 = Int32()
        pri2.data = p2

        self.pos_pub2.publish(pos2)
        self.pri_pub2.publish(pri2)

        pos3 = Pose2D()
        pos3.x = self.x3
        pos3.y = self.y3
        pos3.theta = 0.0

        pri3 = Int32()
        pri3.data = p3

        self.pos_pub3.publish(pos3)
        self.pri_pub3.publish(pri3)

        self.get_logger().info(
            f"R1 ({self.x1:.2f}, {self.y1:.2f}) P={p1} | "
            f"R2 ({self.x2:.2f}, {self.y2:.2f}) P={p2} | "
            f"R3 ({self.x3:.2f}, {self.y3:.2f}) P={p3}"
        )


def main():
    rclpy.init()
    node = FleetEmulator()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
