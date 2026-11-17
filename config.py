"""Central configuration. Change settings here, not inside other files."""
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


class Config:
    # Folders
    UPLOAD_FOLDER = BASE_DIR / "uploads"
    MODEL_DIR = BASE_DIR / "models"
    MODEL_PATH = MODEL_DIR / "voice_detector.joblib"  # created in Stage 3

    # Upload rules
    MAX_CONTENT_LENGTH = 20 * 1024 * 1024  # 20 MB; Flask rejects larger requests (HTTP 413)
    ALLOWED_EXTENSIONS = {"wav", "mp3", "flac", "ogg", "m4a", "webm"}
    UPLOAD_FIELD_NAME = "audio"  # the form-data key the client must use

    # Audio settings (used from Stage 2)
    TARGET_SAMPLE_RATE = 16000  # every file is converted to 16 kHz mono
    MIN_DURATION_SEC = 1.0
    MAX_DURATION_SEC = 60.0

    # Server
    HOST = "0.0.0.0"  # listen on all network interfaces so other devices on the LAN can connect
    PORT = 5000
    DEBUG = True