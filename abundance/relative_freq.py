import pandas as pd
from collections import Counter

# Input taxonomy file
input_csv = "taxonomy/taxonomy_table.csv"
output_csv = "abundance/relative_abundance.csv"

df = pd.read_csv(input_csv)

k = 4  # k-mer size
abundance = []

for _, row in df.iterrows():
    seq_id = row["id"]
    seq = row["sequence"]

    # Count kmers
    kmers = [seq[i:i+k] for i in range(len(seq)-k+1)]
    counts = Counter(kmers)

    total = sum(counts.values())
    rel_freq = {kmer: v/total for kmer, v in counts.items()}

    rel_freq["id"] = seq_id
    rel_freq["Genus"] = row["Genus"]   # Keep virus genus info
    abundance.append(rel_freq)

# Save table
abundance_df = pd.DataFrame(abundance).fillna(0)
abundance_df.to_csv(output_csv, index=False)
print(f"✅ Relative abundance saved to {output_csv}")

