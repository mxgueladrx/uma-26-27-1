import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

class TurtlesimControlNode(Node):
    def __init__(self):
        super().__init__('turtlesim_control_node')
        
        # Log message indicating the node has started
        self.get_logger().info("Turtlesim Control Node is now running...")

        # Subscriber to the /turtle1/pose topic
        self.pose_subscription = self.create_subscription(
            Pose,  # Message type for the /turtle1/pose topic
            '/turtle1/pose',  # Topic name to subscribe to
            self.pose_callback,  # Callback function that processes the message
            10  # QoS queue size
        )
        self.pose_subscription  # Prevent unused variable warning

        # Publisher to the /turtle1/cmd_vel topic
        self.velocity_publisher = self.create_publisher(
            Twist,  # Message type for the /turtle1/cmd_vel topic
            '/turtle1/cmd_vel',  # Topic name to publish to
            10  # QoS queue size
        )

        # Timer to publish velocity commands periodically
        self.timer = self.create_timer(0.5, self.publish_velocity_command)

        # Store the latest pose received from the subscriber
        self.current_pose = None

    def pose_callback(self, msg):
        """
        Callback function for the /turtle1/pose topic.
        Called whenever a new Pose message is received.
        Parameters:
        - msg (Pose): The message containing the turtle's position, orientation, and velocity.
        """
        self.current_pose = msg  # Store the received pose in the node's state
        # Print the pose information to the terminal
        self.get_logger().info(
            f'Turtle Pose - x: {msg.x:.2f}, y: {msg.y:.2f}, theta: {msg.theta:.2f}'
        )

    def publish_velocity_command(self):
        """
        Publishes velocity commands to the /turtle1/cmd_vel topic.
        This method is periodically called by the timer.
        """
        if self.current_pose is not None:  # Ensure we have a valid pose before publishing
            # Create a Twist message to specify linear and angular velocities
            twist = Twist()
            twist.linear.x = 2.0  # Move forward at a speed of 2.0 units/sec
            twist.angular.z = 1.0  # Rotate counterclockwise at a speed of 1.0 rad/sec

            # Publish the velocity command to the /turtle1/cmd_vel topic
            self.velocity_publisher.publish(twist)

            # Log the command for debugging
            self.get_logger().info(f'Published velocity command: {twist}')


def main(args=None):
    """
    Main function to start the node.
    """
    rclpy.init(args=args)  # Initialize the ROS 2 system
    turtlesim_control_node = TurtlesimControlNode()  # Create an instance of the node
    rclpy.spin(turtlesim_control_node)  # Keep the node running until interrupted
    turtlesim_control_node.destroy_node()  # Clean up the node
    rclpy.shutdown()  # Shut down the ROS 2 system


if __name__ == '__main__':
    main()