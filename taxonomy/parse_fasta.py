from Bio import SeqIO
import pandas as pd

# Input FASTA and output CSV
input_fasta = "data/raw/betacoronavirus.fasta"
output_csv = "taxonomy/taxonomy_table.csv"

# Prepare storage
records = []
for record in SeqIO.parse(input_fasta, "fasta"):
    seq_id = record.id
    seq = str(record.seq)

    # Pseudotaxonomy for virus dataset
    taxonomy = {
        "Kingdom": "Virus",
        "Phylum": "Riboviria",         # RNA viruses
        "Class": "Nidovirales",        # order of coronaviruses
        "Order": "Nidovirales",
        "Family": "Coronaviridae",
        "Genus": "Betacoronavirus",
        "Species": "Unknown"
    }

    taxonomy["id"] = seq_id
    taxonomy["sequence"] = seq
    records.append(taxonomy)

# Save as CSV
df = pd.DataFrame(records)
df.to_csv(output_csv, index=False)
print(f"✅ Taxonomy table saved to {output_csv}")
