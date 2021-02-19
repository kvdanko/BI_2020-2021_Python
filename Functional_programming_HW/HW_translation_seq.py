from Bio import SeqIO
from Bio.Seq import Seq

# Path to .fasta file
fasta_path = "/home/katerina/sample.fasta"


# Extraction of sequences and their length from fasta file
def translation(path_to_fasta, codon_table='Standard'):
    fasta_dict = SeqIO.to_dict(SeqIO.parse(path_to_fasta, "fasta"))
    for SeqRecord in fasta_dict.values():
        yield SeqRecord.seq.translate(table=codon_table, to_stop=True)


print(next(translation(fasta_path)))
