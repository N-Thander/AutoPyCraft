
# FastAPI Project 
---


## Project Structure

```
fastapi_project/
├── app/
│   ├── __init__.py
│   ├── main.py          # Entry point (FastAPI app)
│   ├── routes.py        # API routes
│   ├── models.py        # Database models (SQLAlchemy)
│   ├── dependencies.py  # Dependency injection
│   ├── config.py        # Configuration
├── venv/
├── requirements.txt     # Dependencies (fastapi, uvicorn, etc.)
├── .gitignore
├── README.md


```

🔹 Run FastAPI App: ```uvicorn app.main:app --reload```