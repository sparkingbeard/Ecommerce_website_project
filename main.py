from fastapi import FastAPI
from routes import products_controller
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
@app.get("/")
def home():
    return {"message": "Api Running"}


app.include_router(products_controller.router, prefix = "/products")