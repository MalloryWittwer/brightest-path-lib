import os
from pathlib import Path
from setuptools import setup, find_packages
import sys
from transonic.dist import ParallelBuildExt, make_backend_files, init_transonic_extensions

here = Path(__file__).parent.absolute()
sys.path.insert(0, ".")

VERSION = "1.0.1"
TRANSONIC_BACKEND = "pythran"

build_dependencies_backends = {
    "pythran": ["pythran"],
    "cython": ["cython"],
    "python": [],
    "numba": ["numba"],
}


setup_requires = []
setup_requires.extend(build_dependencies_backends[TRANSONIC_BACKEND])


def transonize():
    paths = [
        "brightest_path_lib/cost/reciprocal_transonic.py",
        "brightest_path_lib/heuristic/euclidean_transonic.py"
    ]
    make_backend_files([here / path for path in paths], backend=TRANSONIC_BACKEND)


def create_pythran_extensions():
    import numpy as np

    extensions = init_transonic_extensions(
        # "brightest-path-lib",
        "brightest_path_lib",
        backend=TRANSONIC_BACKEND,
        include_dirs=np.get_include(),
        compile_args=("-O3", f"-march=native", "-DUSE_XSIMD"),
        # compile_args=("-O2", "-DUSE_XSIMD"),
    )
    return extensions


def create_extensions():
    transonize()
    return create_pythran_extensions()


setup(
    name="brightest-path-lib",
    description="A library of path-finding algorithms to find the brightest path between two points.",
    author="Vasudha Jha",
    url="https://github.com/mapmanager/brightest-path-lib",
    project_urls={
        "Issues": "https://github.com/mapmanager/brightest-path-lib/issues",
        "CI": "https://github.com/mapmanager/brightest-path-lib/actions",
        "Changelog": "https://github.com/mapmanager/brightest-path-lib/releases",
    },
    license="GNU General Public License, Version 3",
    version=VERSION,
    #packages=["brightest_path_lib"],
    #packages=find_packages(),
    packages=find_packages(include=[
        "brightest_path_lib",
        "brightest_path_lib.*",
        "brightest_path_lib.algorithm",
        "brightest_path_lib.input"
        ]),
    setup_requires=setup_requires,
    install_requires=["numpy", "transonic"],
    extras_require={
        'dev': [
            'mkdocs',
            'mkdocs-material',
            'mkdocs-jupyter',
            'mkdocstrings',
            'mkdocs-material-extensions'
        ],
        "test": [
            "pytest", 
            "pytest-cov", 
            "scikit-image", 
            "pooch"
        ]
    },
    python_requires=">=3.7",
    cmdclass={"build_ext": ParallelBuildExt},
    ext_modules=create_extensions(),
)
