from fastapi import FastAPI
from routes import products

app = FastAPI()
@app.get("/")
def home():
    return {"message": "Kar diya hit mil gai kaleje ko thandak --- Api Running"}


app.include_router(products.router, prefix = "/products")