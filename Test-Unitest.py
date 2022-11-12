from main import reverse
import unittest

class TestReverse(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(reverse(""),"")

    def test_one_sym(self):
        self.assertEqual(reverse("a"), "a")

    def test_polindrom(self):
        self.assertEqual(reverse("aba"), "aba")

    def test_correct(self):
        self.assertEqual(reverse("abcd"), "dcba")

    def test_type_int(self):
        with self.assertRaises(TypeError):
            reverse(42)

    def test_type_list(self):
        with self.assertRaises(TypeError):
            reverse('c', 'a', 'd')


if __name__ == '__main__':
    unittest.main()
