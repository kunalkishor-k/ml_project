from setuptools import setup, find_packages
from typing import List


PROJECT_NAME = "Machine Learning Project"
VERSION = "0.0.1"
DESCRIPTION ="This is ML project in modular coding"
AUTHOR="KK"
AUTHOR_EMAIL ="kk@gmail.com" 

HYPHEN_E_DOT ="-e ."
# requirement.txt file open
# read
REQUIREMENTS_FILE_NAME = "requirement.txt"
def get_requirement_list()-> List[str]:
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n","") for requirement_name in requirement_list]

        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)

        return requirement_list


setup(name = PROJECT_NAME,
      version= VERSION,
      description= DESCRIPTION,
      author= AUTHOR,
      author_email= AUTHOR_EMAIL,
      packages=find_packages(), # it goes in src folder and find __init__.py file,
      install_requires = get_requirement_list()
)