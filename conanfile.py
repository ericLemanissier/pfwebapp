from conans import ConanFile, CMake
from conans.client import tools


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

    def source(self):
        tools.get(url="https://github.com/ocornut/imgui/archive/v1.85.tar.gz",
            sha256="7ed49d1f4573004fa725a70642aaddd3e06bb57fcfe1c1a49ac6574a3e895a77",
            destination=".",
            strip_root=True)
        tools.get(url="https://github.com/epezent/implot/archive/refs/tags/v0.12.tar.gz",
            sha256="f8bc3b9b58dbabe3a0c0a2ebb8307d8e850012685332a85be36fcc4d4450be56",
            destination=".",
            strip_root=True)

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
