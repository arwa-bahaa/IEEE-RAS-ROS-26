import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Pose2D
from std_msgs.msg import Int32

import random


class FleetEmulator(Node):

    def __init__(self):
        super().__init__('fleet_emulator')

 
        self.declare_parameter('robot_position', '5,5')
        pos = self.get_parameter('robot_position').value

        x, y = pos.split(',')
        self.base_x = float(x)
        self.base_y = float(y)

        self.pos_pub1 = self.create_publisher(Pose2D, 'robot1/position', 10)
        self.pri_pub1 = self.create_publisher(Int32, 'robot1/priority', 10)

        self.pos_pub2 = self.create_publisher(Pose2D, 'robot2/position', 10)
        self.pri_pub2 = self.create_publisher(Int32, 'robot2/priority', 10)

        self.pos_pub3 = self.create_publisher(Pose2D, 'robot3/position', 10)
        self.pri_pub3 = self.create_publisher(Int32, 'robot3/priority', 10)


        self.x1 = self.base_x + random.uniform(-1, 1)
        self.y1 = self.base_y + random.uniform(-1, 1)

        self.x2 = self.base_x + random.uniform(-2, 2)
        self.y2 = self.base_y + random.uniform(-2, 2)

        self.x3 = self.base_x + random.uniform(-1.5, 1.5)
        self.y3 = self.base_y + random.uniform(-1.5, 1.5)

        self.timer = self.create_timer(0.1, self.publish_data)

        self.get_logger().info("Fleet Emulator Started")


    def publish_data(self):

        self.x1 += random.uniform(-0.3, 0.3)
        self.y1 += random.uniform(-0.3, 0.3)

        self.x2 += random.uniform(-0.3, 0.3)
        self.y2 += random.uniform(-0.3, 0.3)

        self.x3 += random.uniform(-0.3, 0.3)
        self.y3 += random.uniform(-0.3, 0.3)

  
        p1 = random.randint(1, 5)
        p2 = random.randint(1, 5)
        p3 = random.randint(1, 5)


        self.pos_pub1.publish(self.make_pose(self.x1, self.y1))
        self.pri_pub1.publish(Int32(data=p1))


        self.pos_pub2.publish(self.make_pose(self.x2, self.y2))
        self.pri_pub2.publish(Int32(data=p2))


        self.pos_pub3.publish(self.make_pose(self.x3, self.y3))
        self.pri_pub3.publish(Int32(data=p3))


        self.get_logger().info(
            f"R1 ({self.x1:.2f}, {self.y1:.2f}) P={p1} | "
            f"R2 ({self.x2:.2f}, {self.y2:.2f}) P={p2} | "
            f"R3 ({self.x3:.2f}, {self.y3:.2f}) P={p3}"
        )


    def make_pose(self, x, y):
        msg = Pose2D()
        msg.x = x
        msg.y = y
        msg.theta = 0.0
        return msg


def main():
    rclpy.init()
    node = FleetEmulator()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
