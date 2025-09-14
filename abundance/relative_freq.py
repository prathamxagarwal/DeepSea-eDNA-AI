# abundance/relative_freq.py
import pandas as pd
import os

kmer_csv = "data/processed/kmer_dataset.csv"
tax_csv = "taxonomy/parsed_with_taxonomy.csv"  # optional
out_rel = "abundance/relative_kmer_freq.csv"
out_tax = "abundance/relative_by_genus.csv"

df = pd.read_csv(kmer_csv)   # each row = sequence id + kmer counts, assume 'id' or 'sequence_id' column
id_col = "id" if "id" in df.columns else ("sequence_id" if "sequence_id" in df.columns else df.columns[0])
kmer_cols = [c for c in df.columns if c!=id_col]

# compute relative freq per sequence
df_rel = df.copy()
df_rel[kmer_cols] = df_rel[kmer_cols].div(df_rel[kmer_cols].sum(axis=1), axis=0).fillna(0)
df_rel.to_csv(out_rel, index=False)
print("Saved", out_rel)

# if taxonomy present, aggregate relative frequency by genus
if os.path.exists(tax_csv):
    tax = pd.read_csv(tax_csv)[["sequence_id","genus"]]
    merged = df.merge(tax, left_on=id_col, right_on="sequence_id", how="left")
    agg = merged.groupby("genus")[kmer_cols].sum()
    agg_rel = agg.div(agg.sum(axis=1), axis=0).fillna(0)
    agg_rel.to_csv(out_tax)
    print("Saved aggregated genus relative freq:", out_tax)
