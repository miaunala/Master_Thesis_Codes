import pandas as pd
import numpy as np
#import spacy
import re

covid= r"C:/Users/.../corona_comments.csv"

df = pd.read_csv(covid)
print(len(df))
df = df.dropna(subset=['raw_text'])
nr_mess = len(df)
print(f"Anzahl Messages: {nr_mess}")
print(df.head())

df.to_csv("C:/Users/.../corona_comments_na_rem.csv")
RANDOM_SEED = 42
np.random.seed(RANDOM_SEED)

# Calculate message counts per account
account_message_counts = df.groupby('channel_name').size()
# asked GPT how to best attribute weights
weights = 1/account_message_counts[df["channel_name"]].values
print(weights)
print(np.sum(weights))
normalised_weights = weights / np.sum(weights)
print(normalised_weights)

# Sample messages - ensure equal probability for each account
sampled_indices = np.random.choice(df.index, size=25000, replace=False, p=normalised_weights)
sampled_df = df.loc[sampled_indices]
print(sampled_df)

sampled_df.to_csv("C:/Users/.../sample_covid_big.csv")
