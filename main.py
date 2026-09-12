from fastapi import FastAPI, File, UploadFile
import pandas as pd

app = FastAPI()

@app.get("/")
def health_check():
    return {"status": "ok", "message": "Python Microservice is running"}

@app.post("/process-excel")
async def process_excel(file: UploadFile = File(...)):
    # 1. Read the Excel file
    df = pd.read_excel(file.file)
    
    # 2. Fix the empty cell issue
    # This replaces all NaN values with a safe, empty string
    df = df.fillna("")
    
    # 3. Return processed records back as JSON
    return df.to_dict(orient="records")
