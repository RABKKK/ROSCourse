# What version of CMake is needed?
cmake_minimum_required(VERSION 2.8.3)

# The name of this package.
project(subscriber_publisher_demo)

# Find the catkin build system, and any other packages on which we depend.
find_package(catkin REQUIRED COMPONENTS roscpp geometry_msgs turtlesim std_srvs)

# Declare our catkin package.
catkin_package()

# Specify locations of header files.
include_directories(include ${catkin_INCLUDE_DIRS})

# Declare the executable, along with its source files.
add_executable(startnode_sample startnode_sample.cpp)
add_executable(pubvel_sample pubvel_sample.cpp)
add_executable(subpose_sample subpose_sample.cpp)

# Specify libraries against which to link.
target_link_libraries(startnode_sample ${catkin_LIBRARIES})
target_link_libraries(pubvel_sample ${catkin_LIBRARIES})
target_link_libraries(subpose_sample ${catkin_LIBRARIES})
