import unittest
from collections.abc import Hashable, Iterable, Iterator
from HW_classes import Rna, Dna


# Tests for Rna class
class RnaClassInitializationTest(unittest.TestCase):

    def test_initialization(self):
        self.assertIsInstance(Rna("AUGC"), Rna)

    @unittest.expectedFailure
    def test_initialization_fail(self):
        self.assertIsInstance(
            Rna("ATGC"),
            Rna,
            "Rna sequence can not contain Thymine")
        self.assertIsInstance(
            Rna("ABCD"),
            Rna,
            "Rna sequence contains unexpected elements")
        self.assertIsInstance(
            Rna(""),
            Rna,
            "Rna sequence is empty")


class RnaClassGCcontentTest(unittest.TestCase):
    seq_rna = 'AU' * 10 + 'GC' * 40

    def test_gc(self):
        self.assertEqual(
            Rna(self.seq_rna).gc_content(),
            "GC-content is 80.0%")


class RnaClassReverseComplementTest(unittest.TestCase):
    seq_rna = "AGAUACACA"

    def test_reverse_complement_function(self):
        self.assertEqual(Rna(self.seq_rna).reverse_complement(),
                         "Complementary sequence is UGUGUAUCU")


class RnaClassIteratorTest(unittest.TestCase):
    seq_rna = "AGAUACACA"

    def test_iter_function(self):
        self.assertIsInstance(Rna(self.seq_rna), Iterable)
        self.assertIsInstance(Rna(self.seq_rna), Iterator)


class RnaClassEqHashTest(unittest.TestCase):
    seq1_rna = "AGAUACACA"
    seq2_rna = "AGAUACACA"
    seq3_rna_fail = "AGAUACCCC"

    def test_eq_function(self):
        self.assertTrue(Rna(self.seq1_rna) == Rna(self.seq2_rna))
        self.assertFalse(Rna(self.seq1_rna) == Rna(self.seq3_rna_fail))

    def test_hash_function(self):
        self.assertIsInstance(Rna(self.seq1_rna), Hashable)


# Tests for Dna class
class DnaClassInitializationTest(unittest.TestCase):

    def test_initialization_dna(self):
        self.assertIsInstance(Dna("ATGC"), Dna)

    @unittest.expectedFailure
    def test_initialization_dna_fail(self):
        self.assertIsInstance(
            Dna("AUGC"),
            Dna,
            "Dna sequence can not contain Uracil")
        self.assertIsInstance(
            Rna("ABCD"),
            Rna,
            "Dna sequence contains unexpected elements")
        self.assertIsInstance(
            Dna(""),
            Dna,
            "Dna sequence is empty")


class DnaClassGCcontentTest(unittest.TestCase):
    seq_dna = 'AT' * 10 + 'GC' * 40

    def test_gc(self):
        self.assertEqual(
            Dna(self.seq_dna).gc_content(),
            "GC-content is 80.0%")


class DnaClassReverseComplementTest(unittest.TestCase):
    seq_dna = "AGATACACA"

    def test_reverse_complement(self):
        self.assertEqual(
            Dna(self.seq_dna).reverse_complement(),
            "Complementary sequence is TGTGTATCT")


class DnaClassTranscribeTest(unittest.TestCase):
    seq_dna = "AGATACACA"

    def test_transcribe_rna(self):
        self.assertEqual(
            Dna(self.seq_dna).transcribe(),
            Rna("UCUAUGUGU"))


class DnaClassIteratorTest(unittest.TestCase):
    seq_dna = "AGATACACA"

    def test_iter_function(self):
        self.assertIsInstance(Dna(self.seq_dna), Iterable)
        self.assertIsInstance(Dna(self.seq_dna), Iterator)


class DnaClassEqHashTest(unittest.TestCase):
    seq1_dna = "AGATACACA"
    seq2_dna = "AGATACACA"
    seq3_dna_fail = "AGATACCCC"

    def test_eq_function(self):
        self.assertTrue(Dna(self.seq1_dna) == Dna(self.seq2_dna))
        self.assertFalse(Dna(self.seq1_dna) == Dna(self.seq3_dna_fail))

    def test_hash_function(self):
        self.assertIsInstance(Dna(self.seq1_dna), Hashable)


if __name__ == '__main__':
    unittest.main()
