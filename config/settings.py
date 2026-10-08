from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DOCUMENT_PATH = BASE_DIR / "documents" / "ecommerce.txt"

VECTOR_DB_PATH = BASE_DIR / "vector_db"
REPORT_FILE = Path("reports/evaluation_report.json")
RETRIEVAL_DATASET = (BASE_DIR/ "testdata"/ "rag"/ "rag_retrieval_dataset.json")

GROUNDING_DATASET = (BASE_DIR/ "testdata"/ "rag"/ "rag_generation_dataset.json")

OLLAMA_MODEL = "qwen2.5:7b"

OLLAMA_BASE_URL = "http://localhost:11434"

TEMPERATURE = 0

THRESHOLD = 0.7