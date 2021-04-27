from setuptools import setup, find_packages

requirements = ['iso8601']

setup(
    name='hlcpy',
    version='0.0.1',
    url='https://github.com/Lamden/hlcpy.git',
    author='JeffWScott',
    author_email='jeff@lamden.io',
    description="Hybrid Logical Clock in Python3.6",
    packages=find_packages(),
    install_requires=requirements,
)
