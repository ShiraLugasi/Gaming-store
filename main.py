from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from enum import Enum

class Game(str, Enum):
    fifa = "FIFA 22"
    cod = "Call of Duty: Warzone"
    rdr2 = "Red Dead Redemption 2"

class RequestBody(BaseModel):
    game: Game
    platform: str
    edition: str

class ResponseBody(BaseModel):
    price: float
    message: str

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Gaming Store"}

@app.post("/get_game_price")
def get_game_price(request_data: RequestBody):
    try:
        game_price_mapping = {
            (Game.fifa, "PC", "standard"): 49.99,
            (Game.fifa, "PS4", "standard"): 59.99,
            (Game.fifa, "Xbox", "standard"): 59.99,
            # Add more game pricing information based on platform and edition
            # ...
        }

        key = (request_data.game, request_data.platform, request_data.edition)
        if key not in game_price_mapping:
            raise HTTPException(status_code=400, detail="Invalid game, platform, or edition")

        price = game_price_mapping[key]
        return {"price": price, "message": f"Price for {request_data.game} ({request_data.edition}) on {request_data.platform}: ${price}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

