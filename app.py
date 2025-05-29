import streamlit as st
from app.core.parser import IngredientParser
from app.core.recommender import RecipeRecommender
from app.db.crud import load_recipes

st.title("🥑 What's in My Fridge?")
st.write("Enter ingredients you have, and get recipe recommendations!")

with st.form("ingredient_input"):
    ingredients_text = st.text_input("Ingredients (comma-separated)", "tomato, cheese, pasta")
    dietary_restrictions = st.multiselect(
        "Dietary Restrictions",
        ["vegetarian", "vegan", "gluten-free"]
    )
    submitted = st.form_submit_button("Find Recipes")

if submitted:
    try:
        # Parse ingredients
        ingredients = IngredientParser.parse(ingredients_text)

        # Load recipes and filter
        recipes = load_recipes()
        filtered_recipes = [
            r for r in recipes
            if all(tag in r.dietary_tags for tag in dietary_restrictions)
        ]

        # Recommend recipes
        recommender = RecipeRecommender(filtered_recipes)
        recommendations = recommender.recommend(" ".join(ingredients))

        # Display results
        st.subheader("Recommended Recipes")
        for recipe in recommendations:
            with st.expander(f"🍲 {recipe.name} (Rating: {recipe.rating or 'N/A'})"):
                st.write(f"**Ingredients:** {', '.join(recipe.ingredients)}")
                st.write(f"**Tags:** {', '.join(recipe.dietary_tags)}")

    except Exception as e:
        st.error(f"Error: {str(e)}")