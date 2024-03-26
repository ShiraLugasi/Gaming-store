from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from DB.DB import SessionLocal, Game


app = FastAPI()

class GameCreate(BaseModel):
    name: str

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:root@postgresdb/postgres"


def get_connection():
    db =SessionLocal()
    try:
        yield db
    finally:
        db.close()
    print("postgres connected")



@app.get("/")
def read_root():
    return {"message": "Welcome to my API"}


@app.post("/games/")
def create_game(game_data: GameCreate):
    db = SessionLocal()
    db_game = Game(name=game_data.name)
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game





