import os
from pathlib import Path
from typing import Optional

def ensure_directory(directory: str) -> None:
    """Ensure a directory exists"""
    Path(directory).mkdir(parents=True, exist_ok=True)

def cleanup_temp_files(directory: str) -> None:
    """Clean up temporary files in a directory"""
    for file in Path(directory).glob("temp_*"):
        file.unlink()

def get_env_variable(key: str, default: Optional[str] = None) -> str:
    """Safely get environment variable"""
    value = os.getenv(key, default)
    if value is None:
        raise ValueError(f"Environment variable {key} not set")
    return value