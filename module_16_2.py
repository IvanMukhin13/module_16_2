from fastapi import FastAPI, Path
from typing import Annotated
import uvicorn

app = FastAPI()


@app.get('/')
async def main_page() -> str:
    return "Главная страница"


@app.get('/user/admin')
async def log_in_admin() -> str:
    return "Вы вошли как администратор"


@app.get('/user/{user_id}')
async def log_in_user(user_id: int = Path(ge=1, le=100, description='Enter User ID', examples=[1])) -> str:
    return f"Вы вошли как пользователь № {user_id}"


@app.get('/user/{username}/{age}')
async def info_user(
        username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', examples=['UrbanUser'])],
        age: Annotated[int, Path(ge=18, le=120, description='Enter age', examples=[22])]) -> str:
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'


if __name__ == '__main__':
    uvicorn.run(app='module_16_2:app', host="127.0.0.1", port=8000, reload=True)
