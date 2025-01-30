from pydantic import BaseModel, Field


class TaskBase(BaseModel):
  title: str | None = Field(default=None, example="クリーニングに行く")


class Task(TaskBase):
  id: int
  done: bool = Field(default=False, description="完了フラグ")
  
  class config:
    orm_mode = True
  

class TaskCreate(TaskBase):
  pass


class TaskCreateResponse(TaskBase):
  id: int
  
  class config:
    orm_mode = True