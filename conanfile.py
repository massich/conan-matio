from conans import ConanFile, CMake, tools


class Matio(ConanFile):
    """Build Conan matio-openmeeg"""
    name = "matio-openmeeg"
    version = "3.10.0"
    url = "https://github.com/massich/conan-matio"
    source_url = "https://github.com/openmeeg/matio-openmeeg"
    commit_id = "ca52f9101046ef6b9d15c6ba799132f96973ea48"
    author = "massich"
    license = "MIT"
    settings = "os", "arch", "compiler", "build_type"
    generators = "cmake"
    exports = "*"
    description = "matio version of openmeeg"
    requires = "hdf5/1.10.1-dm2@sik/testing"
    options = {"shared": [True, False]}
    default_options = "shared=True"

    def source(self):
        self.run("git clone {0}.git".format(self.source_url))
        with tools.chdir("./matio-openmeeg"):
            self.run("git checkout -f {0}".format(self.commit_id))

    def build(self):
        shared = {"BUILD_SHARED_LIBS": self.options.shared}
        cmake = CMake(self)
        with tools.chdir("./matio-openmeeg"):
            cmake.configure(defs=shared)
            cmake.build()

    def package(self):
        self.copy("*.h", dst="include")
        self.copy("*.lib", dst="lib", src="lib", keep_path=False)
        self.copy("*.dll", dst="bin", src="bin", keep_path=False)
        self.copy("*.dylib", dst="bin", src="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["matio-openmeeg"]
