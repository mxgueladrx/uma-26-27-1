sudo apt install ros-jazzy-navigation2 ros-jazzy-nav2-bringup xterm

sudo rosdep init
rosdep update
rosdep install --from-paths src


colcon build --symlink-install

source install/setup.bash
