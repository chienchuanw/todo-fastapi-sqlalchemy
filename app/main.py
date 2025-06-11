from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db, engine, Base
from sqlalchemy import text
from app import models
from contextlib import asynccontextmanager
from app.schemas import TodoResponse, TodoCreate, TodoUpdate
from app.crud import create_todo, get_todo, update_todo, delete_todo
from fastapi.exceptions import HTTPException


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/test")
async def test_connection(db: AsyncSession = Depends(get_db)):
    try:
        await db.execute(text("SELECT 1"))
        return {"status": "ok"}
    except Exception as e:
        return {"status": "error", "message": str(e)}


@app.post("/todo/create", response_model=TodoResponse, status_code=201)
async def create_todo_endpoint(todo: TodoCreate, db: AsyncSession = Depends(get_db)):
    return await create_todo(db, todo)


@app.get("/todo/{todo_id}", response_model=TodoResponse)
async def read_todo_endpoint(todo_id: int, db: AsyncSession = Depends(get_db)):
    todo = await get_todo(db, todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@app.patch("/todo/{todo_id}", response_model=TodoResponse)
async def update_todo_endpoint(
    todo_id: int, todo: TodoUpdate, db: AsyncSession = Depends(get_db)
):
    todo = await update_todo(db, todo_id, todo)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@app.delete("/todo/{todo_id}", response_model=bool, status_code=200)
async def delete_todo_endpoint(todo_id: int, db: AsyncSession = Depends(get_db)):
    if not await delete_todo(db, todo_id):
        raise HTTPException(status_code=404, detail="Todo not found")
    return await delete_todo(db, todo_id)
