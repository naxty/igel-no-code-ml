import pandas as pd
from sklearn.model_selection import train_test_split


columns_to_drop = ["RowNumber", "CustomerId", "Surname", "Geography", "Gender"]
df = pd.read_csv("raw.csv")

df_columns = df.columns
for column in columns_to_drop:
    assert column in df_columns

df.drop(columns_to_drop, inplace=True, axis=1)
train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

train_df.to_csv("data/train.csv", index=False, sep=",")
test_df.to_csv("data/test.csv", index=False, sep=",")