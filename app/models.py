from pydantic import BaseModel
from typing import List

class ErrorDetail(BaseModel):
    row: int
    column: str
    value: str
    error_type: str
    explanation: str

class AnalysisResult(BaseModel):
    total_rows: int
    total_columns: int
    total_errors: int
    errors: List[ErrorDetail]
