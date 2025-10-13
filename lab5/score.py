from pathlib import Path
import json

SCORES_FILE = Path("scores.json")

def load_scores():
    if SCORES_FILE.exists():
        content = SCORES_FILE.read_text(encoding="utf-8")
        if content.strip():
            return json.loads(content)
    return []

def save_score(score):
    scores = load_scores()
    scores.append(score)
    SCORES_FILE.write_text(json.dumps(scores, indent=2), encoding="utf-8")

def delete_scores():
    if SCORES_FILE.exists():
        SCORES_FILE.unlink()
        load_scores()