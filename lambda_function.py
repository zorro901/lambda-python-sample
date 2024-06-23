from fastapi import FastAPI
from pydantic import BaseModel
from mangum import Mangum

class Item(BaseModel):
    name: str
    price: float

app = FastAPI()

@app.get('/')
async def root():
    return {"message": "Hello from lambda"}

@app.get("/uppercase")
async def uppercase(text: str):
    return {"message": text.upper()}

@app.post("/items")
async def create_item(item: Item):
    return item

handler = Mangum(app)