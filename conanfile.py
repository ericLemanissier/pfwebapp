from conans import ConanFile, CMake
from conans.client import tools


class PfWebApp(ConanFile):
    name = "PfWebApp"
    version = "0.0.1"

    settings = "os", "arch", "build_type"

    def build_requirements(self):
        self.build_requires("make/4.3")

    def export_sources(self):
        self.copy("shell_minimal.html")
        self.copy("makefile")
        self.copy("main.cpp")

    def source(self):
        tools.get(url="https://github.com/ocornut/imgui/archive/v1.85.tar.gz",
            sha256="7ed49d1f4573004fa725a70642aaddd3e06bb57fcfe1c1a49ac6574a3e895a77",
            destination=".",
            strip_root=True)
        tools.get(url="https://github.com/epezent/implot/archive/refs/tags/v0.12.tar.gz",
            sha256="f8bc3b9b58dbabe3a0c0a2ebb8307d8e850012685332a85be36fcc4d4450be56",
            destination=".",
            strip_root=True)


    def build(self):
        self.run("%s all IMGUI_DIR=. IMPLOT_DIR=." % self.user_info_build["make"].make, run_environment=True)

    def package(self):
        self.copy("*", src="web", dst="web")

    def deploy(self):
        self.copy("*", src="web", dst="web")
