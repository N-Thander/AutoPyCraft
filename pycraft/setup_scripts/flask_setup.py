
import os
import subprocess

def setup_flask(project_name):
    # Creates a Flask Project
    
    print(f"Setting up a Flask Project: {project_name}")
    
    os.makedirs(f"{project_name}/app/template", exist_ok=True)
    os.makedirs(f"{project_name}/app/static", exist_ok=True)
    
    # Create virtual environment and install Flask
    subprocess.run(["python", "-m", "venv", f"{project_name}/venv"])
    subprocess.run([f"{project_name}/venv/bin/pip", "install", "flask"])
    
    # Create main files
    with open(f"{project_name}/app/__init__.py", "w") as f:
        f.write("from flask import Flask\napp = Flask(__name__)\nfrom app import routes")

    with open(f"{project_name}/app/routes.py", "w") as f:
        f.write("from app import app\n@app.route('/')\ndef home():\n    return 'Hello, Flask!'")

    with open(f"{project_name}/app.py", "w") as f:
        f.write("from app import app\nif __name__ == '__main__':\n    app.run(debug=True)")
        

    print(f"✅ Flask Project '{project_name}' setup complete!")