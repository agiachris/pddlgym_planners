import setuptools

setuptools.setup(
    name='pddlgym_planners',
    version='0.1.0',    
    description='Symbolic planning support with Python',
    url='https://github.com/agiachris/pddlgym_planners',
    author='Tom Silver, Rohan Chitnis, Mohamed Khodeir, Christopher Agia',
    author_email='cagia@stanford.edu',
    packages=setuptools.find_packages(),
    classifiers=["Programming Language :: Python :: 3"],
    python_requires='>=3.8',
)
