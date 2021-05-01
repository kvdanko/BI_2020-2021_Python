import unittest

import HW_classes


class test_class_initialization(unittest.TestCase):

    def test_initialization_rna(self):
        self.assertIsInstance(HW_classes.Rna("AUGC"), HW_classes.Rna)

    def test_initialization_dna(self):
        self.assertIsInstance(HW_classes.Dna("ATGC"), HW_classes.Dna)

    @unittest.expectedFailure
    def test_initialization_rna_fail(self):
        self.assertIsInstance(HW_classes.Rna("ATGC"), HW_classes.Rna)
        self.assertIsInstance(HW_classes.Rna(""), HW_classes.Rna)

    @unittest.expectedFailure
    def test_initialization_dna_fail(self):
        self.assertIsInstance(HW_classes.Dna("AUGC"), HW_classes.Dna)
        self.assertIsInstance(HW_classes.Dna(""), HW_classes.Dna)


class test_gc_content(unittest.TestCase):
    seq_rna = 'AU' * 10 + 'GC' * 40
    seq_dna = 'AT' * 10 + 'GC' * 40

    def test_gc_rna(self):
        self.assertEqual(
            HW_classes.Rna(
                self.seq_rna).gc_content(),
            "GC-content is 80.0%")

    def test_gc_dna(self):
        self.assertEqual(
            HW_classes.Dna(
                self.seq_dna).gc_content(),
            "GC-content is 80.0%")


class test_reverse_complement(unittest.TestCase):
    seq_rna = "AGAUACACA"
    seq_dna = "AGATACACA"

    def test_reverse_complement_rna(self):
        self.assertEqual(
            HW_classes.Rna(
                self.seq_rna).reverse_complement(),
            "Complementary sequence is UGUGUAUCU")

    def test_reverse_complement_dna(self):
        self.assertEqual(
            HW_classes.Dna(
                self.seq_dna).reverse_complement(),
            "Complementary sequence is TGTGTATCT")


class test_transcribe(unittest.TestCase):
    seq_dna = "AGATACACA"

    def test_transcribe_dna(self):
        self.assertEqual(
            HW_classes.Dna(
                self.seq_dna).transcribe(),
            HW_classes.Rna("UCUAUGUGU"))


if __name__ == '__main__':
    unittest.main()
