import unittest
from flatten import flatten

class TestFlatten(unittest.TestCase):

    def test_flat_list(self):
        lista = [1, 2, 3, 4]
        esperado = [1, 2, 3, 4]
        self.assertEqual(flatten(lista), esperado)

    def test_nested_lists(self):
        lista = [1, [2, 3], [4, [5, 6]]]
        esperado = [1, 2, 3, 4, 5, 6]
        self.assertEqual(flatten(lista), esperado)

    def test_mixed_structures(self):
        lista = [1, (2, 3), {'a': 4, 'b': 5}, [6, [7, 8]]]
        esperado = [1, 2, 3, 'a', 4, 'b', 5, 6, 7, 8]
        self.assertEqual(flatten(lista), esperado)

if __name__ == "__main__":
    unittest.main()