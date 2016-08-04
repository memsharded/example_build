from conans import ConanFile, CMake, tools
import os


class ExamplebuildConan(ConanFile):
    requires = "Poco/1.7.3@lasote/stable"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    def build(self):
        cmake = CMake(self.settings)
        shared = "-DBUILD_SHARED_LIBS=ON" if self.options.shared else ""
        self.run('cmake %s %s %s' % (self.conanfile_directory, cmake.command_line, shared))
        self.run("cmake --build . %s" % cmake.build_config)
