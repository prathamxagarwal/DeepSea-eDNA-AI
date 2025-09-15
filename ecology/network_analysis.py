import pandas as pd
from scipy.stats import entropy

input_csv = "abundance/relative_abundance.csv"
output_csv = "ecology/alpha_diversity.csv"

df = pd.read_csv(input_csv)

alpha = []
for _, row in df.iterrows():
    seq_id = row["id"]

    # take only k-mer columns (skip id, Genus)
    freqs = row.drop(["id", "Genus"]).values
    diversity = entropy(freqs)  # Shannon index

    alpha.append({"id": seq_id, "shannon_diversity": diversity})

alpha_df = pd.DataFrame(alpha)
alpha_df.to_csv(output_csv, index=False)
print(f"✅ Alpha diversity saved to {output_csv}")
