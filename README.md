
---

# **AutoPyCraft 🛠️**  

**Automate Python Project Initialization & Structuring**  

<!-- [![PyPI](https://img.shields.io/pypi/v/pycraft?color=blue&label=PyPI)](https://pypi.org/project/pycraft/)   -->
[![License](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://opensource.org/licenses/GPL-3.0)  
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)  

---

## **📌 Overview**  
**PyCraft** is a **CLI tool** that automates the setup of Python projects by creating structured directories, initializing virtual environments, and installing necessary dependencies.  


## **Project Structure**  

```

autopycraft/
├── setup_scripts/
│   ├── __init__.py       # Initializes Flask app
│   ├── routes.py         # Contains API routes
│   ├── models.py         # Database models (if using SQLAlchemy)
│   ├── templates/        # HTML templates (Jinja2)
│   ├── static/           # CSS, JS, images
├── test/                 # test class
├── venv/                 # Virtual environment
├── config.py             # Configuration settings
├── requirements.txt      # Dependencies (flask, etc.)
├── app.py                # Entry point
├── .gitignore
├── README.md


```


















⚡ **Features:**  
✅ **Framework-specific setups** (Flask, FastAPI, Django, Pygame)  
✅ **Automatic directory & virtual environment creation**  
✅ **Dependency installation**  
✅ **Open-source & customizable**  

---

## **🚀 Installation**  

```sh
pip install autopycraft
```

OR install from source:  

```sh
git clone https://github.com/N-Thander/PyCraft.git
cd PyCraft
pip install -e .
```

---

## **📌 Usage**  

After installation, use **PyCraft** from the command line:  

### **🎯 Creating a Flask Project**  
```sh
pycraft setup-flask my_flask_app
```

### **⚡ Creating a FastAPI Project**  
```sh
pycraft setup-fastapi my_fastapi_app
```

### **🎮 Creating a Pygame Project**  
```sh
pycraft setup-pygame my_game
```

### **🛠️ Creating a Django Project**  
```sh
pycraft setup-django my_django_app
```

Each command will:  
✅ Create the project directory  
✅ Initialize a virtual environment  
✅ Install necessary dependencies  
✅ Generate a structured project skeleton  

---🚀 **Automate Python Project Setup with PyCraft!** 🚀  

Let me know if you need any modifications! 🔥
pycraft/templates/
```

---

## **📌 Contributing**  

Contributions are welcome! 🚀 To contribute:  

1. **Fork** this repository.  
2. Clone your fork:  
   ```sh
   git clone https://github.com/your-username/PyCraft.git
   ```
3. Create a new branch:  
   ```sh
   git checkout -b feature-name
   ```
4. Make your changes & commit:  
   ```sh
   git commit -m "Added a new feature"
   ```
5. Push your branch & create a **Pull Request**! 🎉  

---

## **📜 License**  

This project is licensed under the **GNU General Public License v3.0 (GPL-3.0)**.  
See the full license [here](https://opensource.org/licenses/GPL-3.0).  

---

## **📬 Contact**  
💡 Have questions or suggestions? **Reach out!**  
🔗 [GitHub Issues](https://github.com/N-Thander/PyCraft/issues)  

---


## **Note**  
This project is still underdevelopment and no PyPI package has been released yet.


