# TFM_PredictInProd

- Description:
Follow up project to: https://github.com/WolfSchew/TaxiFareModel
A simple linear regression model to try to predict the fare of a NY taxi ride base on the 
pick up and drop off coordinates. This time it is structured to be used in a production environment.
The project is build to host a docker container containing the trained model on the google cloud platform.
The trained model can then be accessed via an API build with FastAPI und run via uvicorn.
An additional project adds the possiblility to create a website as a user interface to access the API and 
get taxi fare predictions: https://github.com/WolfSchew/TaxiFareWebsite

- Data Source:
a kaggle competition for finding a model capable of predicting taxi fares based on based an training data provided here:
https://www.kaggle.com/c/new-york-city-taxi-fare-prediction/

