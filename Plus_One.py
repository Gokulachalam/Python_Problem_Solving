# Example 1:

# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].
# Example 2:

# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].



# digits = [1,2,3]
# number = int(''.join(map(str, digits)))
# # number = int(''.join(map(str,digits)))
# print(number)
# number = number+1
# print(number)
# conv = list(map(int, str(number)))

# print(conv)





import unittest

class TestDigitConversion(unittest.TestCase):

    def setUp(self):
        # Set up any necessary variables or states
        self.digits = [1, 2, 3]

    def test_conversion_from_digits_to_number(self):
        number = int(''.join(map(str, self.digits)))
        self.assertEqual(number, 123)

    def test_increment_number(self):
        number = int(''.join(map(str, self.digits)))
        number += 1
        self.assertEqual(number, 124)

    def test_conversion_from_number_to_digits(self):
        number = int(''.join(map(str, self.digits)))
        number += 1
        conv = list(map(int, str(number)))
        self.assertEqual(conv, [1, 2, 4])

if __name__ == '__main__':
    unittest.main()

