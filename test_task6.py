from unittest import TestCase
from unittest import mock
import task6


def get_input(text):
    return input(text)


class TestPrime(TestCase):

    def setUp(self):
        """Init"""

    def test_input_m(self):
        space_m = "3 4 5"
        self.assertEqual(task6.input_m(space_m), {3, 4, 5})

    def test_input_n(self):
        space_n = "2 7 9"
        self.assertEqual(task6.input_n(space_n), {2, 7, 9})

    def test_listdif(self):
        dif_elem = {3, 12, 7, 5}
        self.assertEqual(task6.listdif(dif_elem), [3, 5, 7, 12])

    def test_input_num_m(self):
        mock.builtins.input = lambda _: "3"
        self.assertEqual(task6.input_num_m(), 3)

    def test_input_num_n(self):
        mock.builtins.input = lambda _: "4"
        self.assertEqual(task6.input_num_n(), 4)

    def tearDown(self):
        """Finish"""

