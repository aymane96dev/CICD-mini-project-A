# tests/test_main.py
import unittest
from main import add

class TestMain(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(5, 5), 10)
        
if __name__ == "__main__":
    unittest.main()
