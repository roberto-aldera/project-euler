cmake_minimum_required(VERSION 3.17)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

add_compile_options(-Wall -Wextra -pedantic -Werror)

project(cpp_src)

add_executable("problem-001"
               "problem-001.cpp")
add_executable("problem-002"
               "problem-002.cpp")
add_executable("problem-003"
               "problem-003.cpp")
add_executable("problem-004"
               "problem-004.cpp")
add_executable("problem-005"
               "problem-005.cpp")
