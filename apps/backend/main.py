from fastapi import FastAPI

from app.api.company import router as company_router

app = FastAPI(title="Sentrava API")

app.include_router(company_router)


@app.get("/")
def root():
    return {"message": "Welcome to Sentrava API"}