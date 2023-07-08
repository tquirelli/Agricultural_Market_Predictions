from fastapi import FastAPI
from pydantic import BaseModel

class Fecha(BaseModel):
    mes: str
    año: int


app = FastAPI()
