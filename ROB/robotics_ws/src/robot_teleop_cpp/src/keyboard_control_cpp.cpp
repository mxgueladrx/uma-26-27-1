#include <rclcpp/rclcpp.hpp>
#include <geometry_msgs/msg/twist.hpp>
#include <termios.h>
#include <unistd.h>
#include <sys/select.h>
#include <iostream>

char read_key(double timeout_sec = 0.1) {
    struct termios oldt, newt;
    tcgetattr(STDIN_FILENO, &oldt);
    newt = oldt;
    newt.c_lflag &= ~(ICANON | ECHO);
    tcsetattr(STDIN_FILENO, TCSANOW, &newt);

    fd_set readfds;
    FD_ZERO(&readfds);
    FD_SET(STDIN_FILENO, &readfds);

    struct timeval tv;
    tv.tv_sec = static_cast<time_t>(timeout_sec);
    tv.tv_usec = static_cast<suseconds_t>((timeout_sec - tv.tv_sec) * 1e6);

    int ret = select(STDIN_FILENO + 1, &readfds, NULL, NULL, &tv);
    char c = 0;
    if (ret > 0 && FD_ISSET(STDIN_FILENO, &readfds)) {
        read(STDIN_FILENO, &c, 1);
    }

    tcsetattr(STDIN_FILENO, TCSANOW, &oldt);
    return c;
}

class KeyboardControlCpp : public rclcpp::Node {
public:
    KeyboardControlCpp() : Node("keyboard_control_cpp") {
        publisher_ = this->create_publisher<geometry_msgs::msg::Twist>("/cmd_vel", 10);
        RCLCPP_INFO(this->get_logger(), "Nodo de teleoperación en C++ inicializado.");
    }

    bool step() {
        char key = read_key(0.05);
        auto twist = geometry_msgs::msg::Twist();

        if (key == 'w') {
            twist.linear.x = 0.5;
            RCLCPP_INFO(this->get_logger(), "Avanzando [W]");
        } else if (key == 's') {
            twist.linear.x = -0.5;
            RCLCPP_INFO(this->get_logger(), "Retrocediendo [S]");
        } else if (key == 'a') {
            twist.angular.z = 1.0;
            RCLCPP_INFO(this->get_logger(), "Giro Izquierda [A]");
        } else if (key == 'd') {
            twist.angular.z = -1.0;
            RCLCPP_INFO(this->get_logger(), "Giro Derecha [D]");
        } else if (key == ' ') {
            twist.linear.x = 0.0;
            twist.angular.z = 0.0;
            RCLCPP_INFO(this->get_logger(), "Parada [Espacio]");
        } else if (key == 3) {
            return false;
        }

        if (key != 0) {
            publisher_->publish(twist);
        }
        return true;
    }

private:
    rclcpp::Publisher<geometry_msgs::msg::Twist>::SharedPtr publisher_;
};

int main(int argc, char * argv[]) {
    rclcpp::init(argc, argv);
    auto node = std::make_shared<KeyboardControlCpp>();

    while (rclcpp::ok()) {
        if (!node->step()) {
            break;
        }
        rclcpp::spin_some(node);
    }

    rclcpp::shutdown();
    return 0;
}