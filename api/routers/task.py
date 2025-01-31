from fastapi import APIRouter
import api.schemas.task as task_schema
from fastapi.responses import Response


router = APIRouter()


@router.get("/tasks", tags=["task"], response_model=list[task_schema.Task])
async def list_tasks():
    return [task_schema.Task(id=1, title="1つ目のTodoタスク")]

@router.post("/tasks", tags=["task"], response_model=task_schema.TaskCreateResponse)
async def create_task(task_body: task_schema.TaskCreate):
    # ** をつけることで、dictをキーワード引数として展開し、task_schema.TaskCreateResponseクラスのコンストラクタに対してdictのkey/valueを渡す→task_body.dict()で{1, title}のような感じで保存、returnではPydanticを使うためJSONで返される
    return task_schema.TaskCreateResponse(id=1, **task_body.dict())

@router.put("/tasks/{task_id}", tags=["task"], response_model=task_schema.TaskCreateResponse)
async def update_task(task_id: int, task_body: task_schema.TaskCreate):
    return task_schema.TaskCreateResponse(id=1, **task_body.dict())

# deleteメソッドの時はreturnで何も返さない
@router.delete("/tasks/{task_id}", tags=["task"], response_model=None)
async def delete_task(task_id: int):
    return Response(status_code=204)