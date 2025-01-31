from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

import api.cruds.task as task_crud
from api.models.task import get_db
import api.schemas.task as task_schema
from fastapi.responses import Response


router = APIRouter()


@router.get("/tasks", tags=["task"], response_model=list[task_schema.Task])
async def list_tasks(db: AsyncSession = Depends(get_db)):
    return await task_crud.get_tasks_with_done(db)
  
# cruds.taskで作ったORMモデルをJSON形式で返す / models.task.TaskをTaskCreateResponseに変換
# TaskCreateResponseでORMを使うように設定されているため、(id, title)を使って自動的にインスタンスを作成
@router.post("/tasks", tags=["task"], response_model=task_schema.TaskCreateResponse)
async def create_task(
  task_body: task_schema.TaskCreate, db: AsyncSession = Depends(get_db)
  ):
    return await task_crud.create_task(db, task_body)

@router.put("/tasks/{task_id}", tags=["task"], response_model=task_schema.TaskCreateResponse)
async def update_task(task_id: int, task_body: task_schema.TaskCreate):
    return task_schema.TaskCreateResponse(id=1, **task_body.dict())

# deleteメソッドの時はreturnで何も返さない
@router.delete("/tasks/{task_id}", tags=["task"], response_model=None)
async def delete_task(task_id: int):
    return Response(status_code=204)