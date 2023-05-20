import unittest

def find_sum(num1, num2):
    sum_of_numbers = num1 + num2
    return sum_of_numbers

class SumTestCase(unittest.TestCase):
    def test_find_sum(self):
        # Test case 1: num1 = 5, num2 = 7
        result = find_sum(5, 7)
        self.assertEqual(result, 12)

        # Test case 2: num1 = -3, num2 = 10
        result = find_sum(-3, 10)
        self.assertEqual(result, 7)

        # Test case 3: num1 = 0, num2 = 0
        result = find_sum(0, 0)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
