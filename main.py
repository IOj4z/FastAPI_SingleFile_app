from fastapi import FastAPI
from pydantic import BaseModel


class Book(BaseModel):
    id: int


class Album(BaseModel):
    id: int


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Home page"}


@app.get("/books")
async def get_books():
    return {"message": "pass"}


@app.get("/books/{id}")
async def get_book(id: int):
    return {"message": "pass"}


@app.post("/books")
async def add_book(b1: Book):
    return {"message": "pass"}


@app.put("/books/{id}")
async def update_book(id: int):
    return {"message": "pass"}


@app.delete("/books/{id}")
async def delete_book(id: int):
    return {"message": "pass"}


@app.get("/albums")
async def get_albums():
    return {"message": "albums"}


@app.get("/albums/{id}")
async def get_album(id: int):
    return {"message": "album"}


@app.post("/albums")
async def create_album(a1: Album):
    return {"message": "add album"}


@app.put("/albums/{id}")
async def update_album(id: int):
    return {"message": "update album"}


@app.delete("/albums/{id}")
async def delete_album(id: int):
    return {"message": "delete album"}

if __name__ == '__main__':
    pass
