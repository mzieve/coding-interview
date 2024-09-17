import unittest

# Given two strings, write a method to decide if one is a permutation of the other.

"""
Questions To Ask
Is the permutation case sensitive?
    'God' not a permutation to 'dog'

Is whitespace significant?
    'god    ' not a permutation to 'god'
"""

# Sorted Method
"""
def is_permutation(stringOne, stringTwo):
    # Check if lengths are equal
    if len(stringOne) != len(stringTwo):
        return False
    
    # Sort each string
    sortedOne = sorted(stringOne)
    sortedTwo = sorted(stringTwo)
    
    # Compare Sorted String
    return sortedOne == sortedTwo
"""

# Time Complexity: O(nlogn)
# Space Complexity: O(n)

# Countdown Method
def is_permutation(stringOne, stringTwo):
    # Check if lengths are equal
    if len(stringOne) != len(stringTwo):
        return False
    
    # Create hash table to map frequencies
    char_freq = {}

    # Increment count first string
    for char in stringOne:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    
    # Decrement count from second string
    for char in stringTwo:
        if char in char_freq:
            char_freq[char] -= 1
        
            if char_freq[char] < 0:
                return False
        else:
            return False
    return all(count == 0 for count in char_freq.values()) 

# Time Complexity: O(n)
# Space Complexity: O(n)

class TestPermutation(unittest.TestCase):
    def test_permutation(self):
        self.assertTrue(is_permutation("dog", "god"))
        self.assertTrue(is_permutation("aabcda", "dabcaa"))
        self.assertFalse(is_permutation("God", "dog"))

if __name__ == '__main__':
    unittest.main()