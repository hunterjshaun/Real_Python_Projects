# main.py
# Import FastAPI for creating the API 
from fastapi import FastAPI

app = FastAPI()  # Create the app object to handle requests and responses

# Create a route to the root endpoint to run the function below 
# and return a JSON response.
# The function below will return a JSON response with a 
# message key and a value of "Hello World"  
@app.get("/")
async def root():
    return {"message": "Hello World"}
