import select
import sys
import termios
import tty

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


def read_key(timeout=0.1):
    """Return the key pressed by the user, or " if none was pressed."""
    settings = termios.tcgetattr(sys.stdin)
    try:
        tty.setraw(sys.stdin.fileno())
        ready, _, _ = select.select([sys.stdin], [], [], timeout)
        return sys.stdin.read(1) if ready else ""
    finally:
        # Always leave the terminal as we found it!
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)

class KeyboardControlNode(Node):
    def __init__(self):
        super().__init__("keyboard_control")

        self.declare_parameter("topic_name", "/cmd_vel")
        topic = self.get_parameter("topic_name").value

        self.velocity_publisher = self.create_publisher(
            Twist,
            "/cmd_vel",
            10
        )

        self.velocidad_lineal = 0.5
        self.velocidad_angular = 1.0

    def mover(self):
        key = read_key(timeout=0.1)
        twist = Twist()

        if key == "w":
            twist.linear.x = self.velocidad_lineal
            self.get_logger().info("Tecla [W]: Avanzando")
        elif key == "s":
            twist.linear.x = -self.velocidad_lineal
            self.get_logger().info("Tecla [S]: Retrocediendo")
        elif key == "a":
            twist.angular.z = self.velocidad_angular
            self.get_logger().info("Tecla [A]: Girando a la izquierda")
        elif key == "d":
            twist.angular.z = -self.velocidad_angular
            self.get_logger().info("Tecla [D]: Girando a la derecha")
        elif key == " ":
            twist.linear.x = 0.0
            twist.angular.z = 0.0
            self.get_logger().info("Tecla [Espacio]: Robot detenido")
        elif key == "\x03":
            return False

        if key != "":
            self.velocity_publisher.publish(twist)
        
        return True

def main(args=None):
    rclpy.init(args=args)
    keayboard_control_node = KeyboardControlNode()
    while rclpy.ok():
        if not keayboard_control_node.mover():
            break
        rclpy.spin_once(keayboard_control_node, timeout_sec=0.0)
    keayboard_control_node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
