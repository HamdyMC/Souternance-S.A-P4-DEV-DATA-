import uvicorn
from fastapi import FastAPI

# from routes.entite import router as EntiteRouter

app = FastAPI()

# app.include_router(EntiteRouter,tags='Entite',prefix="/entite")

@app.get("/items/{item_id}",tags=['test'])
async def read_item(item_id):
    return {"item_id": item_id}
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/",tags=['test'])
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)