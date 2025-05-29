from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from typing import List
from .models import Recipe

class RecipeRecommender:
    def __init__(self, recipes: List[Recipe]):
        self.recipes = recipes
        self.vectorizer = TfidfVectorizer()

    def recommend(self, user_ingredients: str, top_n: int = 3) -> List[Recipe]:
        # Vectorize Recipes
        recipe_texts = ["".join(r.ingredients) for r in self.recipes]
        recipe_vectors = self.vectorizer.fit_transform(recipe_texts)

        #Vectorize user input
        user_vector = self.vectorizer.transform([user_ingredients])

        #Calculate similarity
        similarities = cosine_similarity(user_vector, recipe_vectors).flatten()
        ranked_indices = similarities.argsort()[::-1][:top_n]
        return [self.recipes[i] for i in ranked_indices]
