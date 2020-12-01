from setuptools import setup, find_packages

setup(
    name='specIO install',
    version='0.1.2',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'scipy']
    )