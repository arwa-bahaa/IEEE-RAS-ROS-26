import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Pose2D
from std_msgs.msg import Int32

import math


class TrafficManager(Node):

    def __init__(self):
        super().__init__('traffic_manager')

        # Safety distance
        self.safety_zone = 2.0

        # My Robot
        self.my_x = 5.0
        self.my_y = 5.0
        self.my_priority = 2

        # Robot 1
        self.robot1_pos = None
        self.robot1_priority = None

        # Robot 2
        self.robot2_pos = None
        self.robot2_priority = None

        # Robot 3
        self.robot3_pos = None
        self.robot3_priority = None


        self.create_subscription(
            Pose2D,
            'robot1/position',
            self.robot1_pos_callback,
            10
        )

        self.create_subscription(
            Int32,
            'robot1/priority',
            self.robot1_pri_callback,
            10
        )

        self.create_subscription(
            Pose2D,
            'robot2/position',
            self.robot2_pos_callback,
            10
        )

        self.create_subscription(
            Int32,
            'robot2/priority',
            self.robot2_pri_callback,
            10
        )

        self.create_subscription(
            Pose2D,
            'robot3/position',
            self.robot3_pos_callback,
            10
        )

        self.create_subscription(
            Int32,
            'robot3/priority',
            self.robot3_pri_callback,
            10
        )

        self.timer = self.create_timer(0.2, self.check)

        self.get_logger().info("Traffic Manager Started")

    def robot1_pos_callback(self, msg):
        self.robot1_pos = msg

    def robot1_pri_callback(self, msg):
        self.robot1_priority = msg.data


    def robot2_pos_callback(self, msg):
        self.robot2_pos = msg

    def robot2_pri_callback(self, msg):
        self.robot2_priority = msg.data


    def robot3_pos_callback(self, msg):
        self.robot3_pos = msg

    def robot3_pri_callback(self, msg):
        self.robot3_priority = msg.data

    def check_robot(self, name, pos, priority):

        if pos is None or priority is None:
            return

        distance = math.sqrt(
            (self.my_x - pos.x) ** 2 +
            (self.my_y - pos.y) ** 2
        )

        if distance < self.safety_zone and priority > self.my_priority:

            self.get_logger().warn(
                f"{name}: DANGER | "
                f"Distance = {distance:.2f} m | "
                f"My Priority = {self.my_priority} | "
                f"Other Priority = {priority} | "
                f"Yield!"
            )

        else:

            self.get_logger().info(
                f"{name}: CLEAR | "
                f"Distance = {distance:.2f} m | "
                f"My Priority = {self.my_priority} | "
                f"Other Priority = {priority}"
            )


    def check(self):

        self.check_robot(
            "Robot1",
            self.robot1_pos,
            self.robot1_priority
        )

        self.check_robot(
            "Robot2",
            self.robot2_pos,
            self.robot2_priority
        )

        self.check_robot(
            "Robot3",
            self.robot3_pos,
            self.robot3_priority
        )


def main():

    rclpy.init()

    node = TrafficManager()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
