import pandas as pd

def summarize_dataframe(df: pd.DataFrame) -> dict:
    summary = {
        "num_rows": len(df),
        "num_columns": len(df.columns),
        "columns": list(df.columns),
        "missing_values": df.isnull().sum().to_dict(),
        "numeric_summary": df.describe().to_dict() if not df.select_dtypes(include="number").empty else {},
        "sample_rows": df.head(5).to_dict(orient="records")
    }

    return summary