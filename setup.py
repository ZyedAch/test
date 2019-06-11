from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read()

setup(
    name='test',
    version='v1.0.0',
    requirements=requirements,
    packages=find_packages(),
    url='',
    license='',
    author='Zyed',
    author_email='',
    description='',
    include_package_data=True,
    entry_points={
        'console_scripts': ['build-clusters=project.cli:build_clusters'],
    }
)
