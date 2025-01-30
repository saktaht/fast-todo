from fastapi import APIRouter
import api.schemas.task as task_schema


router = APIRouter()


@router.get("/tasks", tags=["task"], response_model=list[task_schema.Task])
async def list_tasks():
    return [task_schema.Task(id=1, title="1つ目のTodoタスク")]

@router.post("/tasks", tags=["task"])
async def create_task():
    pass

@router.put("/tasks/{task_id}", tags=["task"])
async def update_task():
    pass

@router.delete("/tasks/{task_id}", tags=["task"])
async def delete_task():
    pass