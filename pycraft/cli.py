
import click

from pycraft.setup_scripts import setup_flask
from pycraft.setup_scripts import setup_django

@click()
def cli():
    """PyCraft: Python Project Automation Tool"""
    pass


# Command to set up a Flask project
@click.command()
@click.argument("project_name")
def setup_flask(project_name):
    setup_flask(project_name)


# Commad to setup a Django project
@click.command()
@click.argument("project_name")
def setup_django(project_name):
    setup_django(project_name)


# Command to setup a FastAPI project
@click.command()
@click.argument("project_name")
def setup_fastapi(project_name):
    setup_fastapi(project_name)
    
