from Bio import SeqIO
import os
import pandas as pd
from itertools import product


raw_processed_path=os.path.join("data","processed")

output_csv_path=os.path.join("data","processed","kmer_dataset.csv")

K=3

bases=["A","T","G","C"]
kmer_list=[''.join(p) for p in product(bases,repeat=K)]

def get_kmer_counts(seq, k=K):
    seq = str(seq).upper()
    counts = dict.fromkeys(kmer_list, 0)
    for i in range(len(seq) - k + 1):
        kmer = seq[i:i+k]
        if kmer in counts:
            counts[kmer] += 1
    return counts

# -----------------------------
# Loop through all cleaned FASTA files
# -----------------------------
all_rows = []

for file in os.listdir(raw_processed_path):
    if file.startswith("cleaned_") and (file.endswith(".fasta") or file.endswith(".fa")):
        fasta_file = os.path.join(raw_processed_path, file)
        print(f"📂 Processing {file}...")

        for record in SeqIO.parse(fasta_file, "fasta"):
            counts = get_kmer_counts(record.seq)
            counts['id'] = record.id  # keep sequence ID
            all_rows.append(counts)

# -----------------------------
# Save to CSV
# -----------------------------
df = pd.DataFrame(all_rows)
df.to_csv(output_csv_path, index=False)
print(f"\n✅ K-mer dataset saved to: {output_csv_path}")
