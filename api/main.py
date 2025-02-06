import uvicorn
from fastapi import FastAPI

from api.routers import task, done


app = FastAPI()
app.include_router(task.router, tags=["task"], prefix="/tasks")
app.include_router(done.router, tags=["done"], prefix="/tasks")


@app.get("/")
async def hello():
  return {"message": "hello world!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)