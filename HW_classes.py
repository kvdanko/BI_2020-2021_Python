class Rna:

    def __init__(self, seq="AGUC"):
        self.seq = seq
        if "T" in self.seq:
            raise Exception("Rna sequence can not contain Thymine")

    def __repr__(self):
        return "Sequence of transcript is " + self.seq

    def gc_content(self):
        count = 0
        for n in self.seq:
            if n == "C" or n == "G":
                count += 1
        return f"GC-content is {count / len(self.seq) * 100}%"

    def reverse_complement(self):
        complement = {'A': 'U', 'C': 'G', 'G': 'C', 'U': 'A'}
        return "Complementary sequence is " + \
            ''.join([complement[n] for n in self.seq])

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < len(self.seq):
            self.n += 1
            return self.seq[self.n - 1]
        else:
            raise StopIteration


class Dna:

    def __init__(self, seq="AGTC"):
        self.seq = seq
        if "U" in self.seq:
            raise Exception("Dna sequence can not contain Uracil")

    def gc_content(self):
        count = 0
        for n in self.seq:
            if n == "C" or n == "G":
                count += 1
        return f"GC-content is {count / len(self.seq) * 100}%"

    def reverse_complement(self):
        complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
        return "Complementary sequence is " + \
            ''.join([complement[n] for n in self.seq])

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < len(self.seq):
            self.n += 1
            return self.seq[self.n - 1]
        else:
            raise StopIteration

    def transcribe(self):
        transcript = {'A': 'U', 'C': 'G', 'G': 'C', 'T': 'A'}
        return Rna(''.join([transcript[n] for n in self.seq]))
