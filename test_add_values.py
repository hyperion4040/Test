from unittest import TestCase
from Calculator import add_values

class TestAdd_values(TestCase):
    def test_add_values(self):
        assert 6 == add_values(3,3)
