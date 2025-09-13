from Bio import SeqIO
import os

# Paths
raw_data_path = os.path.join("data", "raw")
processed_data_path = os.path.join("data", "processed")

# Make sure processed folder exists
os.makedirs(processed_data_path, exist_ok=True)

# Parameters
MIN_LENGTH = 200  # filter out sequences shorter than this

for file in os.listdir(raw_data_path):
    if file.endswith(".fasta") or file.endswith(".fa") or file.endswith(".fna"):
        raw_file = os.path.join(raw_data_path, file)
        processed_file = os.path.join(processed_data_path, f"cleaned_{file}")

        print(f"\n📂 Processing {file}...")

        sequences = list(SeqIO.parse(raw_file, "fasta"))
        print(f"✅ Original sequences: {len(sequences)}")

        # Remove duplicates by sequence ID
        unique_sequences = {}
        for seq in sequences:
            if seq.id not in unique_sequences:
                unique_sequences[seq.id] = seq

        # Filter by length
        filtered_sequences = [
            seq for seq in unique_sequences.values() if len(seq.seq) >= MIN_LENGTH
        ]

        # Save to new file
        SeqIO.write(filtered_sequences, processed_file, "fasta")
        print(f"✅ After cleaning: {len(filtered_sequences)} saved to {processed_file}")
