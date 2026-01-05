from fastapi import FastAPI, UploadFile, File
import shutil
import os

from app.csv_analyzer import analyze_csv
from app.models import AnalysisResult

app = FastAPI(title="AI Data Cleaning & Explaining Assistant")

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/analyze", response_model=AnalysisResult)
async def analyze_csv_file(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    errors = analyze_csv(file_path)

    return AnalysisResult(
        total_rows=sum(1 for _ in open(file_path)) - 1,
        total_columns=len(errors) if errors else 0,
        total_errors=len(errors),
        errors=errors
    )
