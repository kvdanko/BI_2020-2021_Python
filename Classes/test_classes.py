import unittest
import HW_classes


# Tests for Rna class
class RnaClassInitialization(unittest.TestCase):

    def test_initialization(self):
        self.assertIsInstance(HW_classes.Rna("AUGC"), HW_classes.Rna)

    @unittest.expectedFailure
    def test_initialization_fail(self):
        self.assertIsInstance(
            HW_classes.Rna("ATGC"),
            HW_classes.Rna,
            "Rna sequence can not contain Thymine")
        self.assertIsInstance(
            HW_classes.Rna("ABCD"),
            HW_classes.Rna,
            "Rna sequence contains unexpected elements")
        self.assertIsInstance(
            HW_classes.Rna(""),
            HW_classes.Rna,
            "Rna sequence is empty")


class RnaClassGCcontent(unittest.TestCase):
    seq_rna = 'AU' * 10 + 'GC' * 40

    def test_gc(self):
        self.assertEqual(
            HW_classes.Rna(
                self.seq_rna).gc_content(),
            "GC-content is 80.0%")


class RnaClassReverseComplement(unittest.TestCase):
    seq_rna = "AGAUACACA"

    def test_reverse_complement_function(self):
        self.assertEqual(
            HW_classes.Rna(
                self.seq_rna).reverse_complement(),
            "Complementary sequence is UGUGUAUCU")


class RnaClassIterator(unittest.TestCase):
    seq_rna = "AGAUACACA"

    def test_iter_function(self):
        self.assertListEqual([i for i in HW_classes.Rna(self.seq_rna)], [
                             i for i in self.seq_rna])


class RnaClassEqHash(unittest.TestCase):
    seq1_rna = "AGAUACACA"
    seq2_rna = "AGAUACACA"
    seq3_rna_fail = "AGAUACCCС"

    def test_eq_function(self):
        self.assertEqual(
            HW_classes.Rna(
                self.seq1_rna) == HW_classes.Rna(
                self.seq2_rna),
            self.seq1_rna == self.seq2_rna)

    @unittest.expectedFailure
    def test_eq_functions_fail(self):
        self.assertEqual(
            HW_classes.Rna(
                self.seq1_rna) != HW_classes.Rna(
                self.seq3_rna_fail),
            self.seq1_rna == self.seq3_rna_fail)

    def test_hash_function(self):
        self.assertEqual(
            hash(
                HW_classes.Rna(
                    self.seq1_rna)), hash(
                self.seq1_rna))


# Tests for Dna class
class DnaClassInitialization(unittest.TestCase):

    def test_initialization_dna(self):
        self.assertIsInstance(HW_classes.Dna("ATGC"), HW_classes.Dna)

    @unittest.expectedFailure
    def test_initialization_dna_fail(self):
        self.assertIsInstance(
            HW_classes.Dna("AUGC"),
            HW_classes.Dna,
            "Dna sequence can not contain Uracil")
        self.assertIsInstance(
            HW_classes.Rna("ABCD"),
            HW_classes.Rna,
            "Dna sequence contains unexpected elements")
        self.assertIsInstance(
            HW_classes.Dna(""),
            HW_classes.Dna,
            "Dna sequence is empty")


class DnaClassGCcontent(unittest.TestCase):
    seq_dna = 'AT' * 10 + 'GC' * 40

    def test_gc(self):
        self.assertEqual(
            HW_classes.Dna(
                self.seq_dna).gc_content(),
            "GC-content is 80.0%")


class DnaClassReverseComplement(unittest.TestCase):
    seq_dna = "AGATACACA"

    def test_reverse_complement(self):
        self.assertEqual(
            HW_classes.Dna(
                self.seq_dna).reverse_complement(),
            "Complementary sequence is TGTGTATCT")


class DnaClassTranscribe(unittest.TestCase):
    seq_dna = "AGATACACA"

    def test_transcribe_rna(self):
        self.assertEqual(
            HW_classes.Dna(
                self.seq_dna).transcribe(),
            HW_classes.Rna("UCUAUGUGU"))


class DnaClassIterator(unittest.TestCase):
    seq_dna = "AGATACACA"

    def test_iter_function(self):
        self.assertListEqual([i for i in HW_classes.Dna(self.seq_dna)], [
                             i for i in self.seq_dna])


class DnaClassEqHash(unittest.TestCase):
    seq1_dna = "AGATACACA"
    seq2_dna = "AGATACACA"
    seq3_dna_fail = "AGATACCCC"

    def test_eq_function(self):
        self.assertEqual(
            HW_classes.Dna(
                self.seq1_dna) == HW_classes.Dna(
                self.seq2_dna),
            self.seq1_dna == self.seq2_dna)

    @unittest.expectedFailure
    def test_eq_functions_fail(self):
        self.assertEqual(
            HW_classes.Dna(
                self.seq1_dna) != HW_classes.Dna(
                self.seq3_dna_fail),
            self.seq1_dna == self.seq3_dna_fail)

    def test_hash_function(self):
        self.assertEqual(
            hash(
                HW_classes.Dna(
                    self.seq1_dna)), hash(
                self.seq1_dna))


if __name__ == '__main__':
    unittest.main()
