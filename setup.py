from setuptools import setup
import os

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="brightest-path-lib",
    description="A library of path-finding algorithms to find the brightest path between two points.",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Vasudha Jha",
    url="https://github.com/mapmanager/brightest-path-lib",
    project_urls={
        "Issues": "https://github.com/mapmanager/brightest-path-lib/issues",
        "CI": "https://github.com/mapmanager/brightest-path-lib/actions",
        "Changelog": "https://github.com/mapmanager/brightest-path-lib/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["brightest_path_lib"],
    install_requires=[],
    extras_require={"test": ["pytest"]},
    python_requires=">=3.7",
)