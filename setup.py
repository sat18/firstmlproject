## setup is reponsible for crreating my ML applicationn as a package and deploy it and anybody can insatll and use it 

from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT ='-e .'
def get_requirements(file_path:str)->List[str]:

    '''
     this fuction will return list of rerquirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        #while importing req from req.txt it all print '\n' so replace it with space 
        requirements=[req.replace("\n"," ") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            
    return requirements        




setup(
    name='mlproject',
    version ='0.0.1',
    author='satvik',
    author_email='nagarsatvik@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)