# To define the configuration of your project, suxh as its metadata, dependencies, and more

from setuptools import find_packages,setup
# from typing import List

def get_requirements():

    # this will return list of requirements

    requirement_list = []

    try:
        with open('requirements.txt', 'r') as file:
            ## read line in the file
            lines = file.readlines()

            ## process each line
            for line in lines:
                requirement = line.strip()
                ## to ignore empty space and '-e .'
                if requirement and requirement != '-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("The Requirements File not found")
    
    return requirement_list

print(get_requirements())

setup(
    name="Network_Security",
    version="0.0.1",
    author="Likhit",
    author_email="kotho2001@gmail.com",
    packages=find_packages(),
    install_required=get_requirements()
)