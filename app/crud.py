from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Todo
from app.schemas import TodoCreate, TodoUpdate


async def create_todo(db: AsyncSession, todo: TodoCreate):
    db_todo = Todo(**todo.model_dump())
    db.add(db_todo)
    await db.commit()
    await db.refresh(db_todo)
    return db_todo


async def get_todo(db: AsyncSession, todo_id: int):
    return await db.get(Todo, todo_id)


async def update_todo(db: AsyncSession, todo_id: int, todo: TodoUpdate):
    db_todo = await db.get(Todo, todo_id)
    if db_todo:
        update_data = todo.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_todo, key, value)
        db.add(db_todo)
        await db.commit()
        await db.refresh(db_todo)

    return db_todo


async def delete_todo(db: AsyncSession, todo_id: int):
    db_todo = await db.get(Todo, todo_id)
    if db_todo:
        await db.delete(db_todo)
        await db.commit()
        return True
    return False
