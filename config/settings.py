from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
REPORT_DIR = BASE_DIR / "reports"

TEST_DATA_FILE = DATA_DIR / "test_data.json"
REPORT_FILE = REPORT_DIR / "evaluation_report.json"

# DeepEval configuration
THRESHOLD = float(os.getenv("EVAL_THRESHOLD", "0.7"))

# Ollama configuration
OLLAMA_MODEL = os.getenv(
    "OLLAMA_MODEL",
    "qwen2.5:7b"
    #"qwen2.5-coder:1.5b"
)

OLLAMA_BASE_URL = os.getenv(
    "OLLAMA_BASE_URL",
    "http://localhost:11434"
    #"http://172.40.0.50:11434/"
)

# Evaluation settings
TEMPERATURE = float(
    os.getenv("TEMPERATURE", "0")
)

# Make sure report directory exists
REPORT_DIR.mkdir(
    parents=True,
    exist_ok=True
)