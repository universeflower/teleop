################################################################################
# Set minimum required version of CMake, project name and compile options
################################################################################
cmake_minimum_required(VERSION 3.5)
project(turtlebot3_teleop)

################################################################################
# Find packages
################################################################################
find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(std_msgs REQUIRED)

################################################################################
# Build
################################################################################
# Python 스크립트를 실행 가능한 대상으로 지정
ament_python_install_package(${PROJECT_NAME})

################################################################################
# Install
################################################################################
install(DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}/
)

################################################################################
# Declare executables
################################################################################
add_executable(turtlebot3_teleop_key turtlebot3_teleop/turtlebot3_teleop_key.py)

################################################################################
# Specify dependencies for executables
################################################################################
ament_target_dependencies(turtlebot3_teleop_key rclpy std_msgs geometry_msgs)

################################################################################
# Install executables
################################################################################
install(TARGETS
  turtlebot3_teleop_key
  DESTINATION lib/${PROJECT_NAME}
)

################################################################################
# Test
################################################################################
ament_package()

