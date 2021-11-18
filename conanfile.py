from conans import ConanFile, CMake


class PfWebApp(ConanFile):
    name = "PfWebApp"
    version = "0.0.1"

    settings = "os", "arch", "compiler", "build_type"

    generators = "cmake", "cmake_find_package_multi"

    def requirements(self):
        self.requires("imgui/1.85")
        self.requires("implot/0.11")

    def export_sources(self):
        self.copy("shell_minimal.html")
        self.copy("*.cpp")
        self.copy("*.h")
        self.copy("CMakeLists.txt")

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.configure()
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()

    def deploy(self):
        self.copy("*", src="bin", dst="web")
