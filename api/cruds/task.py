from sqlalchemy.ext.asyncio import AsyncSession

import api.models.task as task_model
import api.schemas.task as task_schema


async def create_task(
  db: AsyncSession,
  task_create: task_schema.TaskCreate
) -> task_model.Task:
  task = task_model.Task(**task_create.dict()) # ORMモデルを作成
  db.add(task)
  await db.commit()
  await db.refresh(task) # idを取得、最新のデータを反映
  return task # SQLAlchemyのORMモデルを返す