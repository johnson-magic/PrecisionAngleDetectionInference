cmake_minimum_required(VERSION 3.10)

# 设置项目名称
project(ONNXInference)
set(CMAKE_BUILD_TYPE Release)

option(SPEED_TEST "SPEED TEST" OFF)
option(CONFORMANCE_TEST "conformance test" OFF)
option(ENCRYPT "encrypt" OFF)
if(SPEED_TEST)
    add_definitions(-DSPEED_TEST)
endif()
if(CONFORMANCE_TEST)
    add_definitions(-DCONFORMANCE_TEST)
endif()
if(ENCRYPT)
    add_definitions(-DENCRYPT)
endif()

# 查找 OpenCV 包
list(APPEND CMAKE_PREFIX_PATH "${CMAKE_SOURCE_DIR}/build/build/generators/")
find_package(OpenCV REQUIRED)
find_package(onnxruntime REQUIRED)

# # 根据操作系统设置不同的路径
# if (WIN32)
#     # Windows 上的设置
#     set(ONNXRUNTIME_INCLUDE_DIR "C:/Users/24601/Desktop/fabu/software/onnxruntime-win-x64-1.20.1/onnxruntime-win-x64-1.20.1/include")
#     set(ONNXRUNTIME_LIB_DIR "C:/Users/24601/Desktop/fabu/software/onnxruntime-win-x64-1.20.1/onnxruntime-win-x64-1.20.1/lib")
#     set(ONNXRUNTIME_LIB "onnxruntime.lib")
# else()
#     # Linux 上的设置
#     set(ONNXRUNTIME_INCLUDE_DIR "/home/ecs-user/ultralytics/examples/YOLOv8-ONNXRuntime-CPP/onnxruntime-linux-x64-1.15.1/include/")
#     set(ONNXRUNTIME_LIB_DIR "/home/ecs-user/ultralytics/examples/YOLOv8-ONNXRuntime-CPP/onnxruntime-linux-x64-1.15.1/lib/")
#     set(ONNXRUNTIME_LIB "libonnxruntime.so")
# endif()

# # 包含 ONNX Runtime 的头文件
# include_directories(${ONNXRUNTIME_INCLUDE_DIR})

# # 包含opencv的头文件
# include_directories(${OPENCV_INCLUDE_DIR})

# 设置可执行文件名
set(SOURCES
    main.cpp
    inferencer.cpp
    plugin.cpp
    utils.cpp
)
set(SOURCES_LIBRARY
    inferencer.cpp
    plugin.cpp
    utils.cpp
)
add_library(${PROJECT_NAME}_lib ${SOURCES_LIBRARY})
add_executable(${PROJECT_NAME} ${SOURCES}) # main.cpp 为你的源文件名称
include_directories("./")
include_directories(${OpenCV_INCLUDE_DIRS})
include_directories(${onnxruntime_INCLUDE_DIR})

# 链接 OpenCV 库和 ONNX Runtime 库
target_link_libraries(${PROJECT_NAME} opencv::opencv onnxruntime::onnxruntime)

# 设置 C++ 标准
set_target_properties(${PROJECT_NAME} PROPERTIES
    CXX_STANDARD 17
    CXX_STANDARD_REQUIRED YES)
set_target_properties(${PROJECT_NAME}_lib PROPERTIES
    CXX_STANDARD 17
    CXX_STANDARD_REQUIRED YES)
