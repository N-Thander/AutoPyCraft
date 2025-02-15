
import os 
import subprocess
import shutil

TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), "templates")

def setup_project(framework, project_name):
    """Create Project directory, set up virtual enviromment and install dependencies"""
    project_path = os.path.join(os.getcwd(), project_name)
    
    # copy template
    template_path = os.path.join(TEMPLATES_DIR, f"{framework}_template")
    shutil.copytree(template_path, project_path)
    
    
    # Create Virtual Enviroment 
    venv_path = os.path.join(project_path, "venv")
    subprocess.run(["python", "-m", "venv", venv_path])
    
    # Install dependencies
    subprocess.run([os.path.join(venv_path, "bin", "pip"), "install", "-r", os.path.join(project_path, "requirements.txt")])
    
    # Initialize Git
    subprocess.run(["git", "init", project_path])
    
        
    print(f"✅ {framework} project '{project_name}' setup complete!")
    
    