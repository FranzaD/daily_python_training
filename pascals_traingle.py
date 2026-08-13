# Leetcode Question 25: Pascal's Triangle
# Solved: 8/13/2026
# Big O Notation: O(n) runtime,
# Easy
# https://leetcode.com/problems/pascals-triangle/

# Learned: It is worth tracing through the first set of cases and looking for a pattern to determine proper ranges for indices and loops
# if not enough rows are traced through the overall pattern is diifficult to get right
# opt for using loops if possible before jumping to recursion

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        p_triangle = [[1],[1,1]]
        
        # base cases
        if numRows == 1:
            return [p_triangle[0]]
        if numRows == 2:
            return p_triangle

        #creates the new row intializing the correct number of elements as 1s, +1 since end is exclusive
        for row in range(2, numRows):
            #creates new row, initializing all values as one and then appends it to pascals triangle
            p_triangle.append([1]*(row+1))
            
            #iterates through each index that who's value needs to be updated in current row
            for i in range(0, row-1):
                p_triangle[row][i+1]=p_triangle[row-1][i]+p_triangle[row-1][i+1]
        
        return p_triangle