from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/")
def health_check():
    return {"status": "ok", "message": "Python Microservice is running"}

@app.post("/process")
def process_data(payload: list[dict]):
    # Convert incoming JSON data to a Pandas DataFrame
    df = pd.DataFrame(payload)
    
    # Example processing: clean/transform your data
    # Return processed records back as JSON
    return df.to_dict(orient="records")
