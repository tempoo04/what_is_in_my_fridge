import pandas as pd
from typing import List, Dict
from pathlib import Path
import json
import ast

def load_raw_data() -> pd.DataFrame:
    """Load the raw recipe datased (CSV)"""
    data_path = Path(__file__).parent / "RAW_recipes.csv"
    return pd.read_csv(data_path)

def clean_ingredient(ingredient: str) -> str:
    """Remove quotes and brackets from individual ingredients"""
    ingredient = ingredient.replace("'", "").replace('"', "").replace("[", "").replace("]", "")
    # Handle cases where multiple items got stuck together
    if ' ' in ingredient.strip():
        # Take the last part if there are remnants (e.g., "winter squash" from "[winter squash")
        ingredient = ingredient.strip().split()[-1]
    return ingredient.strip()

def preprocess_recipes(df: pd.DataFrame) -> List[Dict]:
    """Convert raw data into List[Recipe] format"""
    recipes = []
    for _, row in df.iterrows():

        try:
            tags = ast.literal_eval(row["tags"])
        except:
            tags = []

        raw_ingredients = row["ingredients"].strip("[]").split(",")

        # Clean each ingredient
        cleaned_ingredients = [
            clean_ingredient(ing)
            for ing in raw_ingredients
            if clean_ingredient(ing)  # Skip empty strings
        ]

        recipes.append({
            "id": row["id"],
            "name": row["name"],
            "ingredients": cleaned_ingredients,
            "dietary_tags": tags,
            "rating": None
        })

    return recipes

def save_processed_recipes(recipes: List[Dict]):
    """Save processed data to recipes.json"""
    output_path = Path(__file__).parent / "processed_recipes.json"
    with open(output_path, "w") as f:
        json.dump(recipes, f, indent=2)



if __name__ == "__main__":
    df = load_raw_data()
    print("Data loaded")
    recipes = preprocess_recipes(df)
    print("Preprocessing done")
    save_processed_recipes(recipes)
    print("Saved processed recipes")



