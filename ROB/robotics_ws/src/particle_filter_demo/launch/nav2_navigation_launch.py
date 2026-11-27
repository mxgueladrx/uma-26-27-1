# Nav2 navigation servers (planner, controller, behaviors and BT navigator) for the warehouse demo.
# Localization (map_server + AMCL) is launched by navigation_launch.py.
from launch import LaunchDescription
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterFile
from ros2launch.api import get_share_file_path_from_package


def generate_launch_description():
    params = ParameterFile(
        get_share_file_path_from_package(package_name="particle_filter_demo", file_name="nav2_params.yaml"),
        allow_substs=True,
    )
    nodes = ["controller_server", "planner_server", "behavior_server", "bt_navigator"]
    packages = {"controller_server": "nav2_controller", "planner_server": "nav2_planner",
                "behavior_server": "nav2_behaviors", "bt_navigator": "nav2_bt_navigator"}

    ld = LaunchDescription()
    for name in nodes:
        ld.add_action(Node(package=packages[name], executable=name, name=name, output="screen",
                           parameters=[params]))
    ld.add_action(Node(
        package="nav2_lifecycle_manager",
        executable="lifecycle_manager",
        name="lifecycle_manager_nav2",
        parameters=[{"autostart": True}, {"node_names": nodes}],
    ))
    return ld
