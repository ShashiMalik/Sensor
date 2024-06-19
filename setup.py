from setuptools import setup,find_packages
from typing import List 

""" This function will return a list of requirements"""
def get_requirements()->List[str]:
    requirements_list:List[str] = []
    return requirements_list

setup(
    name="Sensor_Fault_Detection",
    version="0.0.1",
    author="Shashi",
    author_email="shashi.ahlawat2@gmail.com",
    packages= find_packages(),
    install_requires = get_requirements()
)