from setuptools import find_packages
from setuptools import setup

setup(
    name='gengo',
    version='0.0.1',
    author='Raymond Ng',
    packages=find_packages(),
    include_package_data=True,
    install_requires=(
        'flask',
    ),
)

