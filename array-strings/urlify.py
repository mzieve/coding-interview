import unittest

"""
Write a method to replace all spaces in a string with '%20'. 
You may assume that the string has sufficent space at the end to hold the additional characters, and that you are given the "true"
length of the string. 

EXAMPLE
Input:  'Mr John Smith    ", 13
Output: 'Mr%20John%20Smith"
"""

def urlify(string, true_length):
    # Convert string into a list
    char_list = list(string)

    # Count spaces in string
    spaces = char_list[:true_length].count(' ')
    
    # Extend list to true length
    char_list = list(string[:true_length]) + [''] * (spaces * 2)

    # Create index to true length
    index = true_length - 1 + spaces * 2

    # Alter the string in reverse order
    for i in range(true_length - 1, -1, -1):
        if char_list[i] == ' ':
            char_list[index] = '0'
            char_list[index - 1] = '2'
            char_list[index - 2] = '%'
            index -= 3
        else:
            # Move the current pointer
            char_list[index] = char_list[i]
            index -= 1

    return ''.join(char_list)

# Time Complexity: O(n)
# Space Complexity: O(n)

class TestPermutation(unittest.TestCase):
    def test_standard_case(self):
        self.assertEqual(urlify('Mr John Smith    ', 13), 'Mr%20John%20Smith')

    def test_no_spaces(self):
        self.assertEqual(urlify('HelloWorld', 10), 'HelloWorld')

    def test_only_spaces(self):
        self.assertEqual(urlify('     ', 5), '%20%20%20%20%20')

    def test_trailing_spaces(self):
        self.assertEqual(urlify('Trailing space     ', 14), 'Trailing%20space')

    def test_empty_string(self):
        self.assertEqual(urlify('', 0), '')

    def test_single_character(self):
        self.assertEqual(urlify('A', 1), 'A')

    def test_single_space(self):
        self.assertEqual(urlify(' ', 1), '%20')

if __name__ == '__main__':
    unittest.main()


