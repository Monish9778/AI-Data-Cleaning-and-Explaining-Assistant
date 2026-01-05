import pandas as pd
from typing import List
from app.models import ErrorDetail

def analyze_csv(file_path: str) -> List[ErrorDetail]:
    df = pd.read_csv(file_path)
    errors = []

    for column in df.columns:
        if pd.api.types.is_numeric_dtype(df[column]):
            for index, value in df[column].items():

                if pd.isna(value):
                    errors.append(ErrorDetail(
                        row=index + 1,
                        column=column,
                        value="NULL",
                        error_type="Missing Integer",
                        explanation="This value is missing but the column expects an integer."
                    ))

                elif not float(value).is_integer():
                    errors.append(ErrorDetail(
                        row=index + 1,
                        column=column,
                        value=str(value),
                        error_type="Invalid Integer",
                        explanation="This value is not a valid integer."
                    ))

        else:
            # Non-numeric column containing numbers as text
            for index, value in df[column].items():
                if isinstance(value, str) and value.isdigit():
                    errors.append(ErrorDetail(
                        row=index + 1,
                        column=column,
                        value=value,
                        error_type="Wrong Data Type",
                        explanation="This value looks like an integer but is stored as text."
                    ))

    return errors
