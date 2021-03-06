import pandas as pd
from statistics import mean

df = pd.read_csv("/home/katerina/PycharmProjects/pandas_data/train.csv", na_values="NaN")
mean_match = mean(df['matches'])
df.query('matches > @mean_match')
train_part = df[["pos", "reads_all", "mismatches", "deletions", "insertions"]]
train_part.to_csv(r"train_part.csv", index=False)