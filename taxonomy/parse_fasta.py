# taxonomy/parse_fasta.py
from Bio import SeqIO
import os
import csv

raw = "data/processed"   # cleaned FASTA files live here
out_csv = "taxonomy/parsed_sequences.csv"

rows = []
for fn in os.listdir(raw):
    if fn.startswith("cleaned_") and fn.endswith((".fasta",".fa",".fna")):
        path = os.path.join(raw, fn)
        for rec in SeqIO.parse(path, "fasta"):
            rows.append([rec.id, rec.description, str(rec.seq), len(rec.seq)])

os.makedirs("taxonomy", exist_ok=True)
with open(out_csv, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["sequence_id","header","sequence","length"])
    writer.writerows(rows)

print("Wrote:", out_csv, "rows:", len(rows))
