from fastapi import APIRouter


router = APIRouter()


@router.get("/tasks", tags=["task"])
async def list_tasks():
    pass

@router.post("/tasks", tags=["task"])
async def create_task():
    pass

@router.put("/tasks/{task_id}", tags=["task"])
async def update_task():
    pass

@router.delete("/tasks/{task_id}", tags=["task"])
async def delete_task():
    pass