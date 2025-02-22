from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

import api.cruds.task as task_crud
from api.models.task import get_db
import api.schemas.task as task_schema


router = APIRouter()

@router.get("/", response_model=list[task_schema.Task])
async def list_tasks(db: AsyncSession = Depends(get_db)):
    return await task_crud.get_tasks_with_done(db)
  
  
# cruds.taskで作ったORMモデルをJSON形式で返す / models.task.TaskをTaskCreateResponseに変換
# TaskCreateResponseでORMを使うように設定されているため、(id, title)を使って自動的にインスタンスを作成
@router.post("/", response_model=task_schema.TaskCreateResponse)
async def create_task(
  task_body: task_schema.TaskCreate, db: AsyncSession = Depends(get_db)
  ):
    return await task_crud.create_task(db, task_body)


@router.put("/{task_id}", response_model=task_schema.TaskCreateResponse)
async def update_task(
  task_id: int, task_body: task_schema.TaskCreate, db: AsyncSession = Depends(get_db)
  ):
    task = await task_crud.get_task(db, task_id=task_id)
    if task is None:
      raise HTTPException(status_code=404, detail="Task Not Found")
    
    return await task_crud.update_task(db, task_body, original=task)
    
    
# deleteメソッドの時はreturnで何も返さない
@router.delete("/{task_id}", response_model=None)
async def delete_task(task_id: int, db: AsyncSession = Depends(get_db)):
    task = await task_crud.get_task(db, task_id=task_id)
    if task is None:
      raise HTTPException(status_code=404, detail="Task Not Found")
    
    return await task_crud.delete_task(db, original=task)