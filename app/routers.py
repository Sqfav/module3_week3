from fastapi import HTTPException, APIRouter
from typing import List

from app.data import db_users
from app.models import User, UserUpdate


router = APIRouter()


# Получение списка всех пользователей
@router.get("/users/", response_model=List[User])
async def read_users():
    return db_users


# Получение пользователя по его ID
@router.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int):
    user = next((user for user in db_users if user.id == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# Создание пользователя
@router.post("/users/", response_model=User)
async def create_user(user: User):
    next_id = max(user.id for user in db_users) + 1
    user.id = next_id
    db_users.append(user)
    return user


# Обновление данных пользователя по id
@router.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, update: UserUpdate):
    user = next((user for user in db_users if user.id == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    for attr_name, attr_value in update.dict().items():
        if attr_value is not None:
            setattr(user, attr_name, attr_value)

    return user


# Удаление пользователя по его ID.
@router.delete("/users/{user_id}")
async def update_user(user_id: int):
    user = next((user for user in db_users if user.id == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db_users.remove(user)
    return {"Ответ": "Пользователь удален"}
