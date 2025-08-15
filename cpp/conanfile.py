import os
import sys
from conan import ConanFile
from conan.tools.files import copy
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps


class ExampleRecipe(ConanFile):
    name = "PrecisionAngleDetectionInference"
    version = "1.0.0"
    
    # Optional metadata
    license = "<Put the package license here>"
    author = "<johnson-magic> <zhangteng@sjtu.edu.cn>"
    url = "<https://github.com/johnson-magic/PrecisionAngleDetectionInference>"
    description = "<general inference library and demo of detector>"
    topics = ("<deeplearning>", "<detector>", "<inference>")
    
    settings = "os", "compiler", "build_type", "arch"
    # generators = "CMakeDeps", "CMakeToolchain"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    # Sources are located in the same place as this recipe, copy them to the recipe
    
    def export_sources(self):
        copy(self, "CMakeLists.txt", src=os.path.join(self.recipe_folder, "detector_inference"), dst=os.path.join(self.export_sources_folder))
        copy(self, "*", src=os.path.join(self.recipe_folder, "detector_inference", "src"), dst=os.path.join(self.export_sources_folder, "src"))
        copy(self, "*", src=os.path.join(self.recipe_folder, "detector_inference", "include"), dst=os.path.join(self.export_sources_folder, "include"))

    def requirements(self):
        self.requires("opencv/4.11.0")
        self.requires("onnxruntime/1.15.1")

    def layout(self):
        cmake_layout(self)
        
    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    # def package_info(self):
    #     self.cpp_info.libs = ["detector_inference"]