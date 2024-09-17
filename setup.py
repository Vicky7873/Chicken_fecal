import os
import setuptools
from pathlib import Path
from setuptools import setup, find_packages

setuptools.setup(
    name="Chicken_fecal",
    version="0.0.1",
    author="Bhikipallai",
    author_email="vicky.pallai900@gmail.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[]
)