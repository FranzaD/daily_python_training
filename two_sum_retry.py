class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # creates empty dictionary to store key value pairs of indices and their numbers from nums
        nums_dict = {}
        
        # iterates through nums retrieving indices and values putting them in the dictionary until the end of nums array
        for curr_index, curr_number in enumerate(nums):
            
            # determines what curr_number needs to be found in dict
            other_number = target - curr_number
            
            # check if other number exists in nums_dict as a key, if yes, return the value of that key
            if other_number in nums_dict:
                return curr_index, nums_dict[other_number]
            
            # puts the current number, index pair into the dictionary
            nums_dict[curr_number] = curr_index
        