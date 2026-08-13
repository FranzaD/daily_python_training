# Leetcode Question 25: Pascal's Triangle
# Solved: 
# Big O Notation: O() runtime,
# Easy
# https://leetcode.com/problems/pascals-triangle/

# Learned:

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # base cases
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]

        # call a function to create the next row necessary
        # say numRows is 5, but we have only the first 2 rows, so then I need to build up to 5
        # so 5-2 = 3, (numRows - 2) gets passed into the function?
        starting_row = numRows-2

        self.generate(starting_row):
            new_row = [1]*starting_row
            p_triangle.append(starting_row)

            for i in range(1, starting_row):
                p_triangle[starting_row][i] = p_triangle[starting_row-1][i-1] + p_triangle[starting_row-1][i] 
            if starting_row == numRows:
                return p_triangle
            else:
                self.generate(starting_row+1)
        # but I need to build up to 5, so then I need to build row 3, row 4, and then row 5. I can't jsut jump into row 5

        #end when starting row = numRow