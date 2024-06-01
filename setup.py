from setuptools import setup, find_packages

REQUIREMENTS = []

setup(
    name="test-package-root",
    version="0.1.0",
    packages=find_packages(),
    install_requires=REQUIREMENTS,
)
