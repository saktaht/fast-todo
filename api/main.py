import uvicorn
from fastapi import FastAPI

from api.routers import task, done


app = FastAPI()
app.include_router(task.router)
app.include_router(done.router)


@app.get("/")
async def hello():
  return {"message": "hello world!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)