from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "name": "Sentrava API",
        "version": "1.0.0",
        "status": "running"
    }