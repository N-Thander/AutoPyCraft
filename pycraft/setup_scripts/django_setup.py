
import os
import subprocess

def setup_django(project_name):
    """Creates a Django Project Structure"""
    
    print(f"Setting up a Django Project: {project_name}")
    
    os.makedirs(project_name, exist_ok=True)    

    # Create virtual environment and install Django
    subprocess.run(["python", "-m", "venv", f"{project_name}/venv"])
    subprocess.run([f"{project_name}/venv/bin/pip", "install", "django"])

    # Initialize Django project
    subprocess.run([f"{project_name}/venv/bin/django-admin", "startproject", project_name, project_name])

    print("✅ Django project setup complete!")