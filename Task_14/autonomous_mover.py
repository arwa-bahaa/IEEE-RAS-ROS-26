import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist


class AutonomousMover(Node):

    def __init__(self):
        super().__init__('autonomous_mover')

        self.publisher = self.create_publisher(
            Twist,
            '/cmd_vel',
            10
        )

        self.timer = self.create_timer(
            0.1,
            self.move_robot
        )

        self.state = 0
        self.counter = 0

        self.get_logger().info(
            'Autonomous mover started'
        )


    def move_robot(self):

        msg = Twist()

        self.counter += 1

        # Move forward
        if self.state == 0:
            msg.linear.x = 0.2
            msg.angular.z = 0.0

            if self.counter > 50:
                self.state = 1
                self.counter = 0


        # Rotate
        elif self.state == 1:
            msg.linear.x = 0.0
            msg.angular.z = 0.5

            if self.counter > 30:
                self.state = 0
                self.counter = 0


        self.publisher.publish(msg)


def main(args=None):

    rclpy.init(args=args)
  
    node = AutonomousMover()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()


