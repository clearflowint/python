from fastapi import FastAPI, File, UploadFile
import pandas as pd

app = FastAPI()

@app.get("/")
def health_check():
    return {"status": "ok", "message": "Python Microservice is running"}

@app.post("/process-excel")
async def process_excel(file: UploadFile = File(...)):
    # Use the file.file attribute to access the raw Python file object
    # Pandas can read this directly into a DataFrame
    df = pd.read_excel(file.file)
    
    # Example processing: clean/transform your data here
    
    # Return processed records back as JSON
    return df.to_dict(orient="records")
