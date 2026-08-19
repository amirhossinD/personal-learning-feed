import json
from pathlib import Path


PROFILE_PATH = Path(__file__).parent.parent / "data" / "learning_profile.json"


def load_profile():
    with open(PROFILE_PATH, "r", encoding="utf-8") as file:
        return json.load(file)