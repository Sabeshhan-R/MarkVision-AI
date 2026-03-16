import pandas as pd
import os

def export_excel(data):
    """
    Exports student marksheet data to an Excel file.
    Expects a list of dictionaries, each containing 'board', 'name', 'total', 'subjects', and 'filename'.
    """
    rows = []

    for student in data:
        # Basic information - All keys and values capitalized/cleaned
        row = {
            "FILENAME": str(student.get("filename", "N/A")).upper(),
            "BOARD": str(student.get("board", "N/A")).upper(),
            "NAME": str(student.get("name", "N/A")).upper(),
            "TOTAL MARKS": str(student.get("total", "N/A")).upper()
        }

        # Flatten subjects - Normalize subject names to avoid redundant columns (e.g., Chemistry vs CHEMISTRY)
        subjects = student.get("subjects", {})
        if isinstance(subjects, dict):
            for subject, mark in subjects.items():
                clean_subject = str(subject).strip().upper()
                row[clean_subject] = str(mark).strip().upper()
        
        rows.append(row)

    if not rows:
        return None

    df = pd.DataFrame(rows)

    # All headers are already uppercase from row creation, but let's ensure it for safety
    df.columns = [str(col).upper() for col in df.columns]

    # Reorder columns: Metadata first, then alphabetical subjects
    meta_cols = ["FILENAME", "BOARD", "NAME", "TOTAL MARKS"]
    actual_meta = [c for c in meta_cols if c in df.columns]
    subject_cols = sorted([c for c in df.columns if c not in meta_cols])
    
    df = df[actual_meta + subject_cols]

    file_path = "marksheet_results.xlsx"
    df.to_excel(file_path, index=False)

    return file_path