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

# 番号(task_id)を指定したいときに呼び出す関数 / routersでtask_idを指定するときに使う
async def get_task(db: AsyncSession, task_id: int) -> task_model.Task | None:
  result: Result = await db.execute(
    select(task_model.Task).where(task_model.Task.id == task_id)
  )
  task: tuple[task_model.Task] | None = result.first()
  return task[0] if task is not None else None # タスクがあれば、task[0]でタプルからtask_model.Taskを取り出す

# updateの実装
async def update_task(
  db: AsyncSession, task_create: task_schema.TaskCreate, original: task_model.Task
) -> task_model.Task:
  original.title = task_create.title  # 既存のタスクのタイトルを新しい値に更新
  db.add(original)
  await db.commit()
  await db.refresh(original)
  return original

# deleteの実装
async def delete_task(db: AsyncSession, original: task_model.Task) -> None:
  await db.delete(original)
  await db.commit()