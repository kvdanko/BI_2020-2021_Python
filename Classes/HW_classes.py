class Rna:

    def __init__(self, seq):
        self.seq = seq
        if "T" in self.seq:
            raise Exception("Rna sequence can not contain Thymine")
        elif not set(self.seq).issubset(set('AUGC')):
            raise Exception("Rna sequence contains unexpected elements")
        if self.seq == "":
            raise ValueError("Rna sequence is empty")

    def __repr__(self):
        return "Sequence of transcript is " + self.seq

    def gc_content(self):
        gc_number = self.seq.count('C') + self.seq.count('G')
        return f"GC-content is {gc_number / len(self.seq) * 100}%"

    def reverse_complement(self):
        complement = {'A': 'U', 'C': 'G', 'G': 'C', 'U': 'A'}
        return "Complementary sequence is " + \
               ''.join([complement[n] for n in self.seq[::-1]])

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < len(self.seq):
            elem = self.seq[self.n]
            self.n += 1
            return elem
        else:
            raise StopIteration

    def __eq__(self, other):
        return self.seq == other.seq

    def __hash__(self):
        return hash(self.seq)


class Dna:

    def __init__(self, seq):
        self.seq = seq
        if "U" in self.seq:
            raise Exception("Dna sequence can not contain Uracil")
        elif not set(self.seq).issubset(set('ATGC')):
            raise Exception("Dna sequence contains unexpected elements")
        if self.seq == "":
            raise ValueError("Dna sequence is empty")

    def gc_content(self):
        gc_number = self.seq.count('C') + self.seq.count('G')
        return f"GC-content is {gc_number / len(self.seq) * 100}%"

    def reverse_complement(self):
        complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
        return "Complementary sequence is " + \
               ''.join([complement[n] for n in self.seq[::-1]])

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < len(self.seq):
            elem = self.seq[self.n]
            self.n += 1
            return elem
        else:
            raise StopIteration

    def transcribe(self):
        transcript = {'A': 'U', 'C': 'G', 'G': 'C', 'T': 'A'}
        return Rna(''.join([transcript[n] for n in self.seq]))

    def __eq__(self, other):
        return self.seq == other.seq

    def __hash__(self):
        return hash(self.seq)