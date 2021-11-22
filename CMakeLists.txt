cmake_minimum_required(VERSION 3.1)
project(index)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

find_package(imgui REQUIRED)
find_package(implot REQUIRED)
set(CMAKE_VERBOSE_MAKEFILE ON)

add_executable(${PROJECT_NAME} main.cpp imgui_impl_sdl.cpp imgui_impl_opengl3.cpp)
target_link_libraries(${PROJECT_NAME} imgui::imgui)
target_link_libraries(${PROJECT_NAME} implot::implot)

target_compile_definitions(${PROJECT_NAME} PRIVATE IMGUI_DISABLE_FILE_FUNCTIONS)
target_compile_options(${PROJECT_NAME} PRIVATE -sUSE_SDL=2)
target_link_options(${PROJECT_NAME} PRIVATE -sUSE_SDL=2  -sALLOW_MEMORY_GROWTH=1 --shell-file shell_minimal.html -sNO_FILESYSTEM=1 --bind -O3)
set_target_properties(${PROJECT_NAME} PROPERTIES SUFFIX ".html")

install(TARGETS ${PROJECT_NAME}
  RUNTIME DESTINATION bin
  LIBRARY DESTINATION lib
  ARCHIVE DESTINATION lib)

install(FILES
  ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/${PROJECT_NAME}.js
  ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/${PROJECT_NAME}.wasm
  DESTINATION bin)
