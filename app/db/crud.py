import json
from pathlib import Path
from typing import List
from ..core.models import Recipe

def load_recipes() -> List[Recipe]:
    db_path = Path(__file__).parent / "recipes.json"
    with open(db_path, "r") as f:
        return [Recipe(**item) for item in json.load(f)]