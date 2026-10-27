"""Environment-backed settings; defaults make the local Ollama setup turnkey."""

import os
from pathlib import Path

from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parents[2]
# Load local overrides first; fill remaining values from the checked-in template.
load_dotenv(PROJECT_ROOT / ".env")
load_dotenv(PROJECT_ROOT / ".env.example")


class Settings:
    """Runtime settings read from environment variables."""

    app_name = "Origin: AI World API"
    ollama_base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    # The selected shared model comes from .env or its .env.example template value.
    ollama_model = os.getenv("OLLAMA_MODEL", "").strip()
    ollama_timeout_seconds = float(os.getenv("OLLAMA_TIMEOUT_SECONDS", "20"))
    decision_interval_seconds = float(os.getenv("DECISION_INTERVAL_SECONDS", "1.2"))
    # Request all layers on GPU; a GPU allocation failure may retry once using RAM/CPU.
    ollama_gpu_layers = 999
    # One simulation month takes one real minute at the default 1x speed.
    # Accept the former variable during migration for existing local environments.
    month_length_seconds = float(os.getenv("MONTH_LENGTH_SECONDS", os.getenv("DAY_LENGTH_SECONDS", "60")))
    natural_event_probability = float(os.getenv("NATURAL_EVENT_PROBABILITY", "0.01"))
    disease_emergence_probability = float(os.getenv("DISEASE_EMERGENCE_PROBABILITY", "0.002"))
    max_saved_events = int(os.getenv("MAX_SAVED_EVENTS", "1000"))
    database_path = os.getenv(
        "AI_WORLD_DATABASE",
        str(PROJECT_ROOT / "data" / "world.sqlite3"),
    )


settings = Settings()
