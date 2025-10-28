# Traffic AI System (Hanoi) — CAPS

Novel method: Constraint‑Aware Priority Scheduling (CAPS) with Dynamic Queue Estimation.

## Local
```bash
python -m venv .venv && .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python scripts/make_dummy_video.py
python main.py
```

## Docker
```bash
docker compose up --build
# Dashboard at http://localhost:8501
```
