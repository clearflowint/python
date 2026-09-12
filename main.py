from fastapi import FastAPI, File, UploadFile
import pandas as pd
import io
from scripts.feeds_report import process_chalimeda_feeds # Import your new script

app = FastAPI()

@app.get("/")
def health_check():
    return {"status": "ok", "message": "Python Microservice is running"}

@app.post("/process-excel")
async def process_excel(scenario: str = "default", file: UploadFile = File(...)):
    # Read the uploaded file into server memory
    file_bytes = await file.read()
    
    # Route the data based on the scenario requested by n8n
    if scenario == "chalimeda_feeds":
        return process_chalimeda_feeds(file_bytes)
        
    # Default fallback (if no specific scenario is provided)
    df = pd.read_excel(io.BytesIO(file_bytes))
    df = df.fillna("")
    return {"data": df.to_dict(orient="records")}
