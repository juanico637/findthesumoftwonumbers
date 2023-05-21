import unittest

def find_sum(num1, num2):
    sum_of_numbers = num1 + num2
    return sum_of_numbers

class SumTestCase(unittest.TestCase):

    def test_find_sum(self):
        #First Test
        result = find_sum(5, 7)
        self.assertEqual(result, 12)

        #Second Test
        result = find_sum(-3, 10)
        self.assertEqual(result, 7)

if __name__ == '__main__':
    unittest.main()
