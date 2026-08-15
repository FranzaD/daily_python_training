# Leetcode Question 28: Valid Palindrome
# Solved: 
# Big O Notation: O() runtime
# Easy
# https://leetcode.com/problems/valid-palindrome/description/

# Learned:
import string

s = "race a car"
#"A man, a plan, a canal: Panama"
def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    # Commence Cleaning: string must be comprised of nonalphanumeric characters
    def cleanString(s):
        #convert all characters to lower case
        if not s.islower():
            s = s.lower()

        #removes leading and trailing whitespaces
        s = s.strip()

        # removes punctuation from string
        for i in string.punctuation:
            s = s.replace(i, "")

        # removes spaces between characters from string
        for i in s:
            s = s.replace(" ", "")
        
        #returns cleaned string
        return s

    #check if the string needs to be cleaned of unnecessary characters
    # if string only contains alphanumeric characters, check if it is a palindrome
    if s.isalnum():
        palindrome = ""
        for char in s[::-1]:
            palindrome += char
        # checks if string is a palindrome, returns true
        if s == palindrome:
            return True
        else:
            return False
    # string needs to be cleaned if there are nonalphanumeric characters present
    else: 
        return isPalindrome(cleanString(s))

print(isPalindrome(s))
        