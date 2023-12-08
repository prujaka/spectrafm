from fastapi import FastAPI

api = FastAPI()


@api.get("/")
def index():
    """Displays welcome message when API is connected"""
    return {"status": "API connected"}

