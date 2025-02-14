import click
from project_setup .utils import setup_project


@click.command()
@click.argument("framework")
@click.argument("project_name")

def setup(framework, project_name):
    valid_frameworks = ["flask", "fastapi", "pygame"]
    
    if framework not in valid_frameworks:
        click.echo(f"❌ Unsupported framework: {framework}. Choose from {valid_frameworks}")
        return
    
    setup_project(framework, project_name)
    click.echo(f"✅ {framework} project '{project_name}' has been created!")
    
if __name__ == "__main__":
    setup()