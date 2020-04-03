import unittest
import time
from unittest.mock import patch

def my_filter(fn, iterable):
    time.sleep(5)
    return  filter(fn, iterable)

class TestMyFilter(unittest.TestCase):
    #@patch("")
    def test_my_filter(self):
        input_list = [1, 2, 3, 4]
        input_fn = lambda x: x % 2

        result = list(my_filter(input_fn, input_list))

        self.assertIn(1, result)
        self.assertIn(3, result)


if __name__ == '__main__':
        unittest.main()
