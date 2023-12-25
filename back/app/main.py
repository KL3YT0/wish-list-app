import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


WISH_LISTS = [
    {"user_id": 1, "wish_list": ["Собака", "Лошадка", "48 попугеев"]},
    {"user_id": 2, "wish_list": ["Хлеб", "Молоко"]},
    {"user_id": 3, "wish_list": ["Полет на луну"]},
]


app = FastAPI(title="Wish List App")

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/wish-list/{user_id}")
def get_wish_list(user_id):
    print(user_id)

    if not user_id:
        return []

    wish_list = next((x for x in WISH_LISTS if x["user_id"] == int(user_id)), None)

    if not wish_list:
        return []

    return {"wish_list": wish_list["wish_list"]}


def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
