from fastapi import FastAPI
from fastapi.responses import FileResponse

from app.database import engine, Base
from app.routes import router


app = FastAPI(title="Notes API")
app.include_router(router)

@app.get("/")
def homepage():
    return FileResponse("static/index.html")
