import unittest
from collections import defaultdict

"""
Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards
and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words. 
You can ignore casing and on-letter characters.

EXAMPLE
Input:  Tact Coa
Output: True (permiutations: "taco cat", "atco cta", etc.)
"""

# Count Method
def is_palindrome_permutation(string):
    # Count Character Frequency
    char_count = defaultdict(int)

    for char in string.lower():
        if char.isalpha():
            char_count[char] += 1
    
    # Check Odd Counts
    odd_count = 0

    for count in char_count.values():
        if count % 2 != 0:
            odd_count += 1
        if odd_count > 1:
            return False
    
    return True

# Time Complexity: O(n)
# Space Complexity: O(n)

class TestPalindromePermutation(unittest.TestCase):
    def test_permutation(self):
        self.assertTrue(is_palindrome_permutation("dod"))
        self.assertTrue(is_palindrome_permutation("Tact Coa"))
        self.assertFalse(is_palindrome_permutation("abcd"))

if __name__ == '__main__':
    unittest.main()

    
     