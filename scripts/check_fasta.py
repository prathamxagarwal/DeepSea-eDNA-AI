from Bio import SeqIO
import os

raw_data_path=os.path.join("data","raw")

for file in os.listdir(raw_data_path):
    if file.endswith(".fasta") or file.endswith(".fa") or file.endswith(".fna"):
        fasta_file=os.path.join(raw_data_path,file)
        print(f"\n Checking file: {file}")

        sequences=list(SeqIO.parse(fasta_file,"fasta"))
        print(f"Total sequences:{len(sequences)}")

        if len(sequences)>0:
            print(f"First sequence ID: {sequences[0].id}")
            print(f"First sequence length: {len(sequences[0].seq)}")

