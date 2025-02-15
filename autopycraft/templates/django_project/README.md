
# Django Project 
---


## Project Structure

```
django_project/
├── manage.py             # Django CLI tool
├── config/               # Project settings
│   ├── __init__.py
│   ├── settings.py       # Global settings
│   ├── urls.py           # URL routing
│   ├── wsgi.py           # Deployment setup
│   ├── asgi.py           # Async support
├── app/                # Application module
│   ├── __init__.py
│   ├── models.py         # Database models
│   ├── views.py          # Business logic
│   ├── urls.py           # App-specific routes
│   ├── templates/        # HTML templates
│   ├── static/           # Static files
├── Database              # Database
├── venv/                 # Virtual environment
├── requirements.txt
├── .gitignore
├── README.md


```

🔹 Run Django App: ```python manage.py runserver```