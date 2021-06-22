from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from numpy.core.arrayprint import dtype_short_repr
import pandas as pd
import numpy as np
from datetime import datetime
import pytz
import joblib

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
def index():
    return {"greeting": "Hello world"}

@app.get("/predict")
def predict(pickup_datetime,pickup_longitude,pickup_latitude,dropoff_longitude,dropoff_latitude,passenger_count):

    pickup_datetime = datetime.strptime(pickup_datetime, "%Y-%m-%d %H:%M:%S")
    # localize the user datetime with NYC timezone
    eastern = pytz.timezone("US/Eastern")
    localized_pickup_datetime = eastern.localize(pickup_datetime, is_dst=None)
    utc_pickup_datetime = localized_pickup_datetime.astimezone(pytz.utc)
    #create a string from the datetime object
    formatted_pickup_datetime = utc_pickup_datetime.strftime("%Y-%m-%d %H:%M:%S UTC")



    X_pred = pd.DataFrame({
    "key":"2013-07-06 17:18:00.000000119",
    "pickup_datetime": np.array(formatted_pickup_datetime),
    "pickup_longitude": np.array(pickup_longitude, dtype='float64'),
    "pickup_latitude": np.array(pickup_latitude, dtype='float64'),
    "dropoff_longitude": np.array(dropoff_longitude, dtype='float64'),
    "dropoff_latitude": np.array(dropoff_latitude, dtype='float64'),
    "passenger_count": np.array(passenger_count, dtype='int64')
    }, index=(0,))
    

    model = joblib.load('model.joblib')
    prediction = model.predict(X_pred)

    return {
    "prediction":prediction[0]
    } 