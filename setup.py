import setuptools
from pathlib import Path

with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()

install_requires = [
    "gym==0.21.0",
    "imageio>=2.13.3",
    "kiwisolver>=1.3.1",
    "matplotlib>=3.3.4",
    "networkx>=2.5.1",
    "numpy>=1.19.5",
    "Pillow>=8.4.0",
    "pipreq>=0.4",
    "pyparsing>=3.0.6",
    "PyWavelets>=1.1.1",
    "scikit-image>=0.17.2",
    "scipy>=1.5.4",
    f'tarski @ file://localhost/{Path(__file__).parent}/pddlgym_planners/tarski',
]

setuptools.setup(
    name='pddlgym_planners',
    version='0.0.1',    
    author='Tom Silver, Rohan Chitnis, Mohamed Khodeir, Christopher Agia',
    author_email='cagia@stanford.edu',
    description='Symbolic planning support in Python',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/agiachris/pddlgym_planners',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    install_requires=install_requires
)
