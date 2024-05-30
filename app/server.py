from fastapi import FastAPI
import joblib
import pandas as pd
import numpy as np
import datetime

model = joblib.load('app/model.joblib')

app = FastAPI()
@app.get('/')
def index():
    return {'message': 'Hello, World!'}

@app.post('/predict')
def grab_large_iced_americano():
    # Get the current time
    now = datetime.datetime.now()

    # Check if the current time is between 7:00am and 9:00am
    if 7 <= now.hour <= 9:
        # Filter the data to get the large iced Americano
        large_iced_americano = print("Its Time to grab Large Iced Americano")
        return large_iced_americano
    else:
        return None

# Call the function
result = grab_large_iced_americano()
if result is not None:
    print(result.head(1))
else:
    print("It's not between 7:00am and 9:00am. Pick another menu!")
