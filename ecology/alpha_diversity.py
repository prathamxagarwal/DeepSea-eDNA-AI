import pandas as pd
import numpy as np
from scipy.stats import entropy

# Example abundance data
data = {
    "Species_A": [10, 5, 0],
    "Species_B": [0, 8, 2],
    "Species_C": [3, 1, 6]
}

df = pd.DataFrame(data, index=["Sample_1", "Sample_2", "Sample_3"])

for sample, row in df.iterrows():
    counts = row.values.astype(float)  # convert to float
    total = counts.sum()
    if total > 0:
        freqs = counts / total  # normalize to probabilities
        diversity = entropy(freqs, base=2)  # Shannon index
        print(f"{sample}: Shannon diversity = {diversity:.4f}")
    else:
        print(f"{sample}: No species observed")
