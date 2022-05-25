import unittest

from PAP22G01.C14_.sample_3 import is_prime, primes


class TestAreaFunction(unittest.TestCase):

    def test_prim(self):
        self.assertTrue(is_prime(2))

    def test_not_prim(self):
        self.assertFalse(is_prime(4))


if __name__ == "__main__":
    unittest.main()
