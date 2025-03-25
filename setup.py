from setuptools import find_packages,setup
from typing import List

def get_requirements() ->List[str]:
    """
    This function will return list of requirements
    """
    requirements_lst:List[str] = []
    try:
        with open('requirements.txt','r') as file:
            #Read lines from the file
            line = file.readlines()
            # process each line
            for lines in line:
                requirements= lines.strip()
                ## igonre the empty lines and -e.
                if requirements and requirements !='-e .':
                    requirements_lst.append(requirements)
    except FileNotFoundError:
        print("requirements.tx file in not found")

    return requirements_lst

print(get_requirements())



setup(
    name ="NetworkSecurity",
    version="0.0.1",
    author="Nitish kumar",
    author_email="professorernitish@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements()
)
