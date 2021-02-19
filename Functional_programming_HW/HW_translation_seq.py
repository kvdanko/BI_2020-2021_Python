from Bio import SeqIO

# Path to .fasta file
fasta_path = "/path/to/sample.fasta"


# Function for extraction of nucleotide sequences from fasta file and
# their translation into protein sequence
def translation(path_to_fasta, codon_table='Standard'):
    fasta_dict = SeqIO.to_dict(SeqIO.parse(path_to_fasta, "fasta"))
    for SeqRecord in fasta_dict.values():
        yield SeqRecord.seq.translate(table=codon_table, to_stop=True)


print(next(translation(fasta_path)))
