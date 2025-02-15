

import os
import subprocess

def setup_fastapi(project_name):
    # Creates a FastAPI Project
    
    print(f"Setting up a FastAPI Project: {project_name}")
    
    os.makedirs(f"{project_name}/app", exist_ok=True)
    
    # Create virtual environment and install FastAPI
    subprocess.run(["python", "-m", "venv", f"{project_name}/venv"])
    subprocess.run([f"{project_name}/venv/bin/pip", "install", "fastapi"])
    
    # Create main files
    with open(f"{project_name}/app/main.py", "w") as f:
        f.write("from fastapi import FastAPI\napp = FastAPI()\nfrom app import routes")

    with open(f"{project_name}/app/routes.py", "w") as f:
        f.write("from fastapi import APIRouter\nfrom app import app\nrouter = APIRouter()\n@router.get('/')\ndef home():\n    return {'message': 'Hello, FastAPI!'}")

    with open(f"{project_name}/app.py", "w") as f:    
        f.write("from fastapi import FastAPI\nfrom app import router\napp = FastAPI()\napp.include_router(router)")

    print(f"✅ FastAPI Project '{project_name}' setup complete!")