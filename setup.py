from setuptools import setup, find_packages

with open('requirements.txt') as f:
    install_requires = f.read().splitlines()

setup(
    name="markdown-crawler",
    packages=find_packages(exclude=['markdown']),
    include_package_data=True,
    install_requires=install_requires,
)