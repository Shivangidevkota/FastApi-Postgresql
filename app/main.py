from fastapi import FastAPI
import models
import router
from config import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get('/')
async def Home():
    return "Welcome Home"

app.include_router(router.router, prefix="/book", tags=["book"])