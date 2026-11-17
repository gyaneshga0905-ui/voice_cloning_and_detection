# AI Voice Cloning Detection System

Flask backend and web page that classify audio as genuine human speech or AI-generated.

## Setup
    py -3.11 -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt

## Run
    python app.py

Web page: http://127.0.0.1:5000/app

## API
| Endpoint | Method | Purpose |
|---|---|---|
| / | GET | Server running check |
| /api/health | GET | Server and model status |
| /api/upload | POST | Validate an audio file (form field audio) |
| /api/detect | POST | Analyse audio, return label and confidence |

## Folders
| Path | Purpose |
|---|---|
| app.py | Creates the app, registers routes and error handlers |
| config.py | Settings |
| routes/ | HTTP endpoints |
| services/ | Validation, audio decoding, features, model |
| models/ | Trained model (voice_detector.joblib) |
| training/ | Dataset preparation and training scripts |
| frontend/ | Web page (upload, record, results, network timings) |
| tests/ | pytest tests |
| uploads/ | Temporary files, auto-deleted |

## Training
1. Extract ASVspoof 2019 LA to C:\voice-data\LA
2. python training\prepare_dataset.py
3. python training\train.py

Eval result (unseen speakers): accuracy 86.94%, EER 12.88%.

## Tests
    pytest -v

## Limitations
- Trained on ASVspoof 2019 studio audio; laptop-mic recordings may be misclassified.
- Without a model file the API returns 503 MODEL_NOT_TRAINED and never guesses.
- Upload is HTTP over TCP. It is not RTP or real-time VoIP.
