# ecology/alpha_diversity.py
import pandas as pd
import numpy as np
from scipy.stats import entropy
import os

# Input: abundance/relative_by_genus.csv  (rows=genus, cols=k-mers) OR rows=samples
infile = "abundance/relative_by_genus.csv"
out = "ecology/alpha_diversity_by_genus.csv"

df = pd.read_csv(infile, index_col=0)  # index = genus
# Compute Shannon (entropy) across columns for each genus row (if you want per sample, swap orientation)
# Here compute diversity across k-mers per genus (example). Adapt if you want per sample.
div = []
for idx, row in df.iterrows():
    vals = row.values
    shannon = entropy(vals)  # natural log
    # Simpson: 1 - sum(p^2)
    simpson = 1 - np.sum(vals**2)
    div.append([idx, shannon, simpson])

outdf = pd.DataFrame(div, columns=["genus","shannon","simpson"])
outdf.to_csv(out, index=False)
print("Saved:", out)
