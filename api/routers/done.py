from fastapi import APIRouter
from fastapi.responses import Response


router = APIRouter()

# putやdeleteメソッドでresponseが必要ない場合、returnで何も返さない
@router.put("/task/{task_id}/done", tags=["done"], response_model=None)
async def mark_task_as_done(task_id: int):
  return Response(status_code=204)

@router.delete("/task/{task_id}/done", tags=["done"], response_model=None)
async def unmark_task_as_done(task_id: int):
  return Response(status_code=204)