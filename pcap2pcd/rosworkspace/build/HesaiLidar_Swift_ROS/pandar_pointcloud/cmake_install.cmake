# Install script for directory: /home/liubo/personal/project/rosworkspace/src/HesaiLidar_Swift_ROS/pandar_pointcloud

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/liubo/personal/project/rosworkspace/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/pandar_pointcloud" TYPE FILE FILES "/home/liubo/personal/project/rosworkspace/devel/include/pandar_pointcloud/CloudNodeConfig.h")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/pandar_pointcloud" TYPE FILE FILES "/home/liubo/personal/project/rosworkspace/devel/include/pandar_pointcloud/TransformNodeConfig.h")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python3/dist-packages/pandar_pointcloud" TYPE FILE FILES "/home/liubo/personal/project/rosworkspace/devel/lib/python3/dist-packages/pandar_pointcloud/__init__.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "/usr/bin/python3" -m compileall "/home/liubo/personal/project/rosworkspace/devel/lib/python3/dist-packages/pandar_pointcloud/cfg")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python3/dist-packages/pandar_pointcloud" TYPE DIRECTORY FILES "/home/liubo/personal/project/rosworkspace/devel/lib/python3/dist-packages/pandar_pointcloud/cfg")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/liubo/personal/project/rosworkspace/build/HesaiLidar_Swift_ROS/pandar_pointcloud/catkin_generated/installspace/pandar_pointcloud.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/pandar_pointcloud/cmake" TYPE FILE FILES
    "/home/liubo/personal/project/rosworkspace/build/HesaiLidar_Swift_ROS/pandar_pointcloud/catkin_generated/installspace/pandar_pointcloudConfig.cmake"
    "/home/liubo/personal/project/rosworkspace/build/HesaiLidar_Swift_ROS/pandar_pointcloud/catkin_generated/installspace/pandar_pointcloudConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/pandar_pointcloud" TYPE FILE FILES "/home/liubo/personal/project/rosworkspace/src/HesaiLidar_Swift_ROS/pandar_pointcloud/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/pandar_pointcloud" TYPE DIRECTORY FILES "/home/liubo/personal/project/rosworkspace/src/HesaiLidar_Swift_ROS/pandar_pointcloud/include/pandar_pointcloud/")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/pandar_pointcloud" TYPE FILE FILES "/home/liubo/personal/project/rosworkspace/src/HesaiLidar_Swift_ROS/pandar_pointcloud/nodelets.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/pandar_pointcloud/launch" TYPE DIRECTORY FILES "/home/liubo/personal/project/rosworkspace/src/HesaiLidar_Swift_ROS/pandar_pointcloud/launch/")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/pandar_pointcloud/params" TYPE DIRECTORY FILES "/home/liubo/personal/project/rosworkspace/src/HesaiLidar_Swift_ROS/pandar_pointcloud/params/")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/home/liubo/personal/project/rosworkspace/build/HesaiLidar_Swift_ROS/pandar_pointcloud/src/lib/cmake_install.cmake")
  include("/home/liubo/personal/project/rosworkspace/build/HesaiLidar_Swift_ROS/pandar_pointcloud/src/conversions/cmake_install.cmake")

endif()

