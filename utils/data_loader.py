import json
from pathlib import Path


def load_test_data(file_path: Path) -> list: 
# Load LLM evaluation test cases from JSON file.
    

    if not file_path.exists():
        raise FileNotFoundError(
            f"Test data file not found: {file_path}"
        )

    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    if not isinstance(data, list):
        raise ValueError(
            "test_data.json must contain a list of test cases."
        )

    return data