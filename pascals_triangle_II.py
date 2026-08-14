# Leetcode Question 26: Pascal's Triangle II
# Solved: 8/13/2026
# Big O Notation: O(n) runtime
# Easy
# https://leetcode.com/problems/pascals-triangle-ii/description/

# Learned: trace through the loop to determine boundary issues!

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        p_triangle = [[1],[1,1]]
        
        # base cases
        if rowIndex == 0:
            return p_triangle[0]
        if rowIndex == 1:
            return p_triangle[1]

        #creates the new row intializing the correct number of elements as 1s, +1 since end is exclusive
        for row in range(2, rowIndex+1):
            #creates new row, initializing all values as one and then appends it to pascals triangle
            p_triangle.append([1]*(row+1))
            
            #updates values of necessary indices
            for i in range(0, row-1):
                p_triangle[row][i+1]=p_triangle[row-1][i]+p_triangle[row-1][i+1]
        
        return p_triangle[rowIndex]