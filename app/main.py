from fastapi import FastAPI

app = FastAPI(
    title="A simple WMS",
    description="A simple WMS REST API built with FastAPI, SQLAlchemy, and SQLite",
    version="0.1.0",
)

# app.include_router(items.router)

@app.get("/")
async def root():
    return {"message": "Welcome to SimpleWMS!"}