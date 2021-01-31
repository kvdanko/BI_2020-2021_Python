import matplotlib.pyplot as plt
import numpy as np

from Bio import SeqIO

# Path to .fasta file
fasta_path = "/home/katerina/sample.fasta"
seq_length = np.array([])

# Extraction of sequences and their length from fasta file
fasta_dict = SeqIO.to_dict(SeqIO.parse(fasta_path, "fasta"))
for SeqRecord in fasta_dict.values():
    seq_length = np.append(seq_length, len(SeqRecord.seq))

# Visualization of sequences length distribution
plt.hist(seq_length, bins=250)
plt.xlim(0, 5000)
plt.xlabel("Sequence Length")
plt.ylabel("Number of Sequences")
plt.title("Length distribution of fasta sequences")
plt.savefig("Length_distribution.png")
