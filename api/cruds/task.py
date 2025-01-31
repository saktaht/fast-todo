from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.engine import Result

import api.models.task as task_model
import api.schemas.task as task_schema

# create(タスクを作成)
async def create_task(
  db: AsyncSession,
  task_create: task_schema.TaskCreate
) -> task_model.Task:
  task = task_model.Task(**task_create.dict()) # ORMモデルを作成
  db.add(task)
  await db.commit()
  await db.refresh(task) # idを取得、最新のデータを反映
  return task # SQLAlchemyのORMモデルを返す

# read(完了したかどうか取得)
async def get_tasks_with_done(db: AsyncSession) -> list[tuple[int, str, bool]]:
  result: Result = await ( # 非同期でSQLを実行
    db.execute(
      select(
        task_model.Task.id,
        task_model.Task.title,
        # タスクが完了済みか判定 / dones.id = NoneならFalse(未完了) NoneじゃないとTrue(完了)
        task_model.Done.id.isnot(None).label("done"), 
      ).outerjoin(task_model.Done) # Doneテーブルと外部結合
    )
  )
  return result.all() #クエリ結果をリストとして取得