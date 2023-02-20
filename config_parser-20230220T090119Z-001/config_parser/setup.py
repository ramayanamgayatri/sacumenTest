from setuptools import setup, find_packages

setup(
    name='configparser',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'PyYAML==5.4.1'
    ],
    tests_require=[
        'pytest==6.2.4'
    ],
)