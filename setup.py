"""
Setup script for the Leelavati library.
"""
import setuptools

with open('README.md', 'r',encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name='lilavati',
    version='1.0.0',
    packages=setuptools.find_packages(),
    install_requires=[],
    author='Your Name',
    author_email='projectleelavati@gmail.com',
    description='Description of your library',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    url='https://github.com/Project-Leelavati/Leelavati.git',
)
