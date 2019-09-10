from setuptools import setup, find_packages

with open("README.rst", "r") as readme_file:
    readme = readme_file.read()


setup(
    name="python_clicker",
    version="0.0.1",
    author="Bevis",
    description="Python Clicker",
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        'pywin32 >= 1.0;platform_system=="Windows"',
        'pyautogui >= 0.1.0'
    ],
    classifiers=[
        "Programming Language :: Python :: 3.7",
    ],
)