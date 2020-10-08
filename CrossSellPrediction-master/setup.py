from setuptools import find_packages, setup


requirements = []
with open("requirements.txt", "r") as f:
    for line in f.readlines():
        line = line.replace("\n", "")
        requirements.append(line)

setup(
    name='CrossSellPrediction',
    version='0.0.0',
    description='TAIL ',
    author='TAIL Team',
    packages=find_packages(),
    install_requires=requirements
)
