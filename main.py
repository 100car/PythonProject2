# Завдання 3
# Напишіть сервер з такими функціями
# ● hello
#   ○ шлях – /hello/{name}
#   ○ метод – POST
#   ○ повертає {"message": "Привіт, {ім'я}!"}
# ● hello_json
#   ○ шлях – /hello_json
#   ○ метод – POST
#   ○ повертає {"message": "Привіт, {ім'я}!"}
# Для hello_json напишіть модель за допомогою pydantic
# Запустіть сервер
# Напишіть клієнта який робить запити на сервер

from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


@app.post("/hello/{name}")
def hello(name: str):
    return {"message": f"Привіт, {name}!"}


class NameData(BaseModel):
    name: str

@app.post("/hello_json")
def hello_json(name_data: NameData):
    name = name_data.name
    return {"message": f"Привіт, {name}!"}


