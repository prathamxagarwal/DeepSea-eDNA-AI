# ecology/beta_diversity.py
import pandas as pd
from scipy.spatial.distance import pdist, squareform
import os

infile = "abundance/relative_by_genus.csv"
out = "ecology/beta_bray_curtis.csv"
df = pd.read_csv(infile, index_col=0)  # rows=genus
dist = pdist(df.values, metric="braycurtis")
sq = squareform(dist)
pd.DataFrame(sq, index=df.index, columns=df.index).to_csv(out)
print("Saved:", out)
