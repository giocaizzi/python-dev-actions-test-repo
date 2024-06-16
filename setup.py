from setuptools import find_packages, setup

REQUIREMENTS = []

setup(
    name="test-package-root",
    version="0.1.0",
    packages=find_packages(),
    install_requires=REQUIREMENTS,
)
