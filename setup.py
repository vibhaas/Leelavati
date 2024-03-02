from setuptools import setup
with open("README.md","r") as f:
    description=f.read()
setup(name="leelavati",
version="1.0.0",
description="This is a repository to create a python library to implement algorithms given in the book leelavati by Bhaskarachary",
long_description=description,
long_description_conten_type="text/markdown",
packages=["leelavati"],
install_requires=[""]
)