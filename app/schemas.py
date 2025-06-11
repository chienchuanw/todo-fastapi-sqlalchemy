from pydantic import BaseModel
from typing import Optional


class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False


class TodoCreate(TodoBase):
    pass


class TodoUpdate(TodoBase):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None


class TodoResponse(TodoBase):
    id: int

    class Config:
        orm_mode = True
        from_attributes = True
