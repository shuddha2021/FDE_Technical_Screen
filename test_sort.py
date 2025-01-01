import unittest
from sort import sort

class TestSortFunction(unittest.TestCase):
    def test_standard_package(self):
        self.assertEqual(sort(100, 100, 100, 10), "STANDARD")

    def test_bulky_package_only(self):
        self.assertEqual(sort(160, 100, 100, 10), "SPECIAL")
        self.assertEqual(sort(100, 160, 100, 10), "SPECIAL")
        self.assertEqual(sort(100, 100, 160, 10), "SPECIAL")
        self.assertEqual(sort(100, 100, 100, 10), "STANDARD")
        self.assertEqual(sort(100, 100, 100, 10), "STANDARD")

    def test_heavy_package_only(self):
        self.assertEqual(sort(100, 100, 100, 25), "SPECIAL")

    def test_rejected_package(self):
        self.assertEqual(sort(160, 100, 100, 25), "REJECTED")
        self.assertEqual(sort(100, 160, 100, 25), "REJECTED")
        self.assertEqual(sort(100, 100, 160, 25), "REJECTED")
        self.assertEqual(sort(160, 160, 160, 25), "REJECTED")

    def test_edge_cases(self):
        # Volume exactly 1,000,000 cm³
        self.assertEqual(sort(100, 100, 100, 10), "STANDARD")  # 1,000,000 cm³ but dimensions not >=150
        self.assertEqual(sort(100, 100, 100, 20), "SPECIAL")  # mass exactly 20 kg
        self.assertEqual(sort(150, 100, 100, 20), "REJECTED")  # dimension exactly 150 and mass exactly 20

    def test_minimum_values(self):
        self.assertEqual(sort(1, 1, 1, 0.1), "STANDARD")

    def test_large_values(self):
        self.assertEqual(sort(200, 200, 200, 50), "REJECTED")

if __name__ == "__main__":
    unittest.main()
