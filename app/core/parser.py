import spacy
from typing import List

nlp = spacy.load("en_core_web_sm")

class IngredientParser:
    @staticmethod
    def parse(ingredients_text: str) -> List[str]:
        "Parse raw text into a list of standartized ingredients"
        doc = nlp(ingredients_text.lower())
        return [
            token.lemma_ for token in doc
            if token.is_alpha and not token.is_stop
        ]