from setuptools import setup, find_packages

setup(
    name="AutoPyCraft",
    version="0.1.0",
    author="N-Thander",
    description="A CLI tool for automating Python project initialization and structuring",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/N-Thander/PyCraft",
    packages=find_packages(),
    install_requires=[
        "click",
    ],
    entry_points={
        "console_scripts": [
            "pycraft=pycraft.cli:cli",  # Matches pyproject.toml
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
