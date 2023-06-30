from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)-> List[str]:
     '''
     this function will return the list of requirements
     '''
     
     requiremens=[]
     with open(file_path) as file_obj:
         requiremens=file_obj.readlines()
         requiremens=[req.replace("\n","") for req in requiremens]
         
         if HYPEN_E_DOT in requiremens:
             requiremens.remove(HYPEN_E_DOT)
     return requiremens
         
         
setup(
    name='mlproject',
    version="0.0.1",
    author="suprith",
    author_email="korishettarsuprith4@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)