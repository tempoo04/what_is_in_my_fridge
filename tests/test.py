import pandas as pd

pd.set_option('display.max_columns', None)
df = pd.read_csv("../app/db/RAW_recipes.csv")
print(df.head())

