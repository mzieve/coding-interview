import unittest

# Implement an algorithm to determine if a string has all unqiue characters. What if you cannot use additional data structures?

"""
Questions To Ask
Is the string an ASCII or a Unicode String?
    - ASCII 128 characters (8-bit byte)
    - Unicode UTF-8 1-4 bytes (8-bit byte) 

If sting is an ASCII is it extended?
    - Extended ASCII 280 characters
"""

# Brute Force
"""
def is_unique(string):
    # Iterate through string and check if there is more than one of each character.
    for char_one in range(len(string)):
        for char_two in range(char_one + 1, len(string)):
            if string[char_one] == string[char_two]:
                return False
    return True
"""
#Time Complexity O(n^2)
#Space Complexity O(1)  

# Boolean Method
"""
def is_unique(string):
    # ASCII has 128 possible characters
    if len(string) > 128:  # There are only 128 ASCII characters
        return False

    # Create a boolean array of size 128 for ASCII characters
    seen = [False] * 128

    # Check if each character has been seen or not
    for char in string:
        ascii_val = ord(char)
        if seen[ascii_val]:
            return False
        seen[ascii_val] = True

    return True
"""

"""
Time Complexity O(n)
Space Complexity O(1)

Argument: Loop will never iterate through more than 128 characters
Time Complexity O(c)
Space Complexity (c)
c - is the size of the character set
"""

# Reduced space usage method
def is_unique(string):
    # Create bit vector
    checker = 0 

    # Get index of the character
    for char in string:
        val = ord(char) - ord('a')  
        if (checker & (1 << val)) > 0: 
            return False 
         
        # Set the bit 
        checker |= (1 << val)  
    
    return True

#Time Complexity O(n)
#Space Complexity O(1)


class TestIsUnique(unittest.TestCase):
    def test_unique_characters(self):
        self.assertTrue(is_unique('blaze'))
        self.assertTrue(is_unique('abcdefg'))
        self.assertTrue(is_unique('xyz'))

    def test_non_unique_characters(self):
        self.assertFalse(is_unique('blazee'))
        self.assertFalse(is_unique('aabbcc'))

    def test_empty_string(self):
        self.assertTrue(is_unique(''))

    def test_single_character(self):
        self.assertTrue(is_unique('b'))

    """
    def test_max_length_unique(self):
        self.assertTrue(is_unique(''.join(chr(i) for i in range(128))))

    def test_max_length_non_unique(self):
        self.assertFalse(is_unique(''.join(chr(i) for i in range(127)) + 'a'))
    """

if __name__ == '__main__':
    unittest.main()

    