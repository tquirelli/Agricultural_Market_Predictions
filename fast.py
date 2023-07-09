import pandas as pd
from fastapi import FastAPI

import requests

app = FastAPI()


@app.get("/")
def predict(
        Number_one: float,  # 2013-07-06 17:18:00
        Number_two: float,    # -73.950655
        Number_three: float,     # 40.783282
        ):      
    prediction = Number_one + Number_two + Number_three
    
    return {"Estimate_price": prediction}

#@app.get("/get_ejemplo")
#def obtener_elementos():
    #return {"datos": datos}