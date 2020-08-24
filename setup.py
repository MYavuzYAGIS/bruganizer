from setuptools import setup

setup(
    name='bruteorganizer',
    version='0.01',
    description='Á Python based CLI tool to sort your messy folders by their extensions',
    py_modules=['bruganizer'],
    install_requires=['Click','Termcolor','Pyfiglet'],
    entry_points='''
    [console_scripts]
    bruganizer=bruganizer:main
    
    '''
    )