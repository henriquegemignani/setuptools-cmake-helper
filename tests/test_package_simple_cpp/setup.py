import os
from pathlib import Path

import setuptools_cmake_helper
from setuptools import setup

file_dir = Path(__file__).parent.absolute().relative_to(Path().absolute())

cmake_project_dir = os.fspath(file_dir.joinpath("cmake_src"))
custom_include_paths = [
    cmake_project_dir,
]

ext_modules = [
    setuptools_cmake_helper.CMakeExtension(
        "test_package._native",
        [
            os.fspath(file_dir.joinpath("wrap_src", "wrap.c")),
        ],
        cmake_options={
            "dir": cmake_project_dir,
            "targets": {
                "native_test": "lib",
            },
        },
        language="c++",
        extra_compile_args=[],
        extra_objects=[],
    )
]


setup(
    cmdclass={
        "build_ext": setuptools_cmake_helper.CMakeBuild,
    },
    ext_modules=ext_modules,
)