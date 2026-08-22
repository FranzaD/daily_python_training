class Solution:
    def reverseBits(self, n):
        # Convert n to a 32-bit binary string, padded with leading zeros
        binary_str = format(n, '032b')
        
        # Reverse the string
        reversed_str = binary_str[::-1]
        
        # Convert back to an integer, interpreting as base 2
        return int(reversed_str, 2)