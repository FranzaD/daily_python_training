# Leetcode Question 28: Valid Palindrome
# Solved: 6/15/2026
# Big O Notation: O(n) runtime, no nested loops
# Easy
# https://leetcode.com/problems/valid-palindrome/description/

# Learned: How to debug and step through code using break points in vs code, allowing me to quickly find what logic isn't triggering to assist with debugging code

import string

#s = "aA"
#"A man, a plan, a canal: Panama"
#""
def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    # Commence Cleaning: string must be comprised of nonalphanumeric characters
    def cleanString(s):
        #convert all characters to lower case
        s = s.lower()

        #removes leading and trailing whitespaces
        s = s.strip()

        # removes punctuation from string
        for i in string.punctuation:
            s = s.replace(i, "")

        # removes spaces between characters from string
        s = s.replace(" ", "")
        
        #returns cleaned string
        return s

    #check if the string needs to be cleaned of unnecessary characters
    if not s.isalnum() or not s.islower():
        s = cleanString(s)
    
    #reverse string for checking if string is a palindrome
    def reverseString(s):
        reversed_string = ""
        for char in s[::-1]:
            reversed_string += char
        return reversed_string
        
    # checks if string is a palindrome, returns true
    if s == reverseString(s):
        return True
    else:
        return False

print(isPalindrome(s))
        