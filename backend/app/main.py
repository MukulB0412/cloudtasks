# backend/app/main.py

from fastapi import FastAPI
import psycopg2
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI is working ✅"}

@app.get("/db")
def db_check():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS"),
            dbname=os.getenv("DB_NAME")
        )
        conn.close()
        return {"db_status": "Connected ✅"}
    except Exception as e:
        return {"db_status": "❌ Failed", "error": str(e)}

@app.get("/tasks")
def get_tasks():
    return [
        {"id": 1, "title": "Setup Dev Environment"},
        {"id": 2, "title": "Dockerize Backend"},
        {"id": 3, "title": "Connect Frontend"},
    ]
