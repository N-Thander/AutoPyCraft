

from setuptools import setup, find_packages

setup(
    name="AutoPyCraft",  
    version="0.1.0",
    author="N-Thander",
    author_email="nasiruddinthander2002@gmail.com",
    description="A CLI Tool for automating Python project initialization and structuring",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/N-Thander/AutoPyCraft",
    packages=find_packages(),
    install_requires=[
        "click",
    ],
    entry_points={
        "console_scripts": [
            "setup-project=project_setup.cli:setup", 
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    include_package_data=True,
    package_data={
        "project_setup": ["templates/*"],
    },
)
