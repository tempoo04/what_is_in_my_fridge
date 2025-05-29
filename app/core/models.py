from pydantic import BaseModel
from typing import List, Optional

class IngredientRequest(BaseModel):
    ingredients: str

class Recipe(BaseModel):
    id: int
    name: str
    ingredients: List[str]
    dietary_tags: List[str]
    rating: Optional[float] = None