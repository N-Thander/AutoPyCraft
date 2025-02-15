
import os
import subprocess

def setup_pygame(project_name):
    # Creates a Pygame Project
    
    print(f"Setting up a Pygame Project: {project_name}")
    
    os.makedirs(f"{project_name}/app", exist_ok=True)
    
    with open (f"{project_name}/app/__init__.py", "w") as f:
        f.write(''' 
                import pygame
                
                pygame.init()
                screen = pygame.display.set_mode((800, 600))
                running = True
                
                while running:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False 
                            
                
                pygame.quit()               
                
                ''')
        
    # Create virtual environment and install Pygame
    subprocess.run(["python", "-m", "venv", f"{project_name}/venv"])
    subprocess.run([f"{project_name}/venv/bin/pip", "install", "pygame"])
    
    print(f"✅ Pygame Project '{project_name}' setup complete!")