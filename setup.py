'''
The setup.py file is essnential part of packing and distributing python projects.
'''


from setuptools import setup,find_packages
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """
    requirment_list:List[str]= []
    try:
        with open('requirements.txt','r') as file:
            #read lines from the file
            lines = file.readlines()
            #process each line
            for line in lines:
                requirment=line.strip()
                #ignore empty lines and -e .
                if requirment and requirment!='-e .':
                    requirment_list.append(requirment)

    except FileNotFoundError:
        print('requirements.txt file not found')

    return requirment_list


setup(

    name='Network Security',
    version='0.0.1',
    author='Sandeep Bandi',
    author_email='bandisandeep1423@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)
