cmake_minimum_required (VERSION 3.1)
project (RingDecomposerLib VERSION 1.0)

enable_testing()

# external options -- build example
option(BUILD_MINIMAL_EXAMPLE "Build minimal example" OFF)

# external options -- build our RDKix testing tool
option(BUILD_RDKIX_BENCHMARK "Build the Benchmark with RDKix" OFF)

# external options -- build python wrapper
option(BUILD_PYTHON_WRAPPER "Build python wrapper" OFF)

# external options -- python executable
set(PYTHON_EXECUTABLE "" CACHE STRING "Python executable for building of the extension")

if(PYTHON_EXECUTABLE STREQUAL "")
  find_program(PYTHON "python")
else()
  set(PYTHON "${PYTHON_EXECUTABLE}")
endif()

# external options -- python flags
set(PYTHON_FLAGS "" CACHE STRING "Python flags")

# external options -- rdkix include directories
set(RDKIX_INCLUDE_DIR "" CACHE STRING "Rdkix include dir")

# external options -- rdkix include directories
set(RDKIX_LIB_DIR "" CACHE STRING "Rdkix librart dir")

set(SOURCE_DIR "${CMAKE_CURRENT_SOURCE_DIR}/src")
set(LIB_SOURCE_DIR "${SOURCE_DIR}/RingDecomposerLib")
set(PYTHON_SOURCE_DIR "${SOURCE_DIR}/python")

set(SHARED_LIBRARY "RingDecomposerLib")
set(STATIC_LIBRARY "RingDecomposerLibStatic")

set(SHARED_TEST "Test")
set(STATIC_TEST "Test_static")

set(SHARED_MINIMALEXAMPLE "MinimalExample")
set(STATIC_MINIMALEXAMPLE "MinimalExample_static")

set(PYTHON_TEST "${PYTHON_SOURCE_DIR}/test/test.py")
set(TEST_DIR "${CMAKE_CURRENT_SOURCE_DIR}/test")

SET(CMAKE_INSTALL_RPATH "\$ORIGIN/lib")

include_directories(${LIB_SOURCE_DIR})
add_subdirectory("${LIB_SOURCE_DIR}")
add_subdirectory("${SOURCE_DIR}/Test")

if(BUILD_MINIMAL_EXAMPLE)
  add_subdirectory("${SOURCE_DIR}/MinimalExample")
endif()

if(BUILD_RDKIX_BENCHMARK)
  add_subdirectory("${SOURCE_DIR}/RDKixBenchmark")
endif()

if(BUILD_PYTHON_WRAPPER)
  add_subdirectory("${PYTHON_SOURCE_DIR}")
endif()

add_subdirectory("${TEST_DIR}")
