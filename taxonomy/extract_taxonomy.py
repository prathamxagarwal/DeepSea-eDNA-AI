# taxonomy/extract_taxonomy.py
import pandas as pd
import os
import hashlib

in_csv = "taxonomy/parsed_sequences.csv"
out_csv = "taxonomy/parsed_with_taxonomy.csv"

df = pd.read_csv(in_csv)

def pseudo_taxonomy(seq_id):
    # deterministic pseudo-label: hash -> choose genus 0..9
    n = int(hashlib.md5(seq_id.encode()).hexdigest()[:8],16) % 10
    return {
        "kingdom":"Bacteria",
        "phylum": f"Phylum_{n%5}",
        "class": f"Class_{n%4}",
        "order": f"Order_{n%6}",
        "family": f"Family_{n%8}",
        "genus": f"Genus_{n}",
        "species": f"Species_{n}"
    }

tax_rows = []
for _, r in df.iterrows():
    header = str(r["header"])
    # try simple header parse for tax info (if present)
    # e.g., if header contains 'taxid|' or 'organism=' patterns — add parsing rules as needed
    if " " in header:
        # naive example: use first token as genus if it looks like a name
        first = header.split()[0].replace(">", "")
        if len(first) > 3 and first.isalpha():
            t = {"kingdom":"Unknown","phylum":"Unknown","class":"Unknown",
                 "order":"Unknown","family":"Unknown","genus":first,"species":"Unknown"}
        else:
            t = pseudo_taxonomy(r["sequence_id"])
    else:
        t = pseudo_taxonomy(r["sequence_id"])
    tax_rows.append({**r.to_dict(), **t})

out = pd.DataFrame(tax_rows)
out.to_csv(out_csv, index=False)
print("Wrote:", out_csv)
