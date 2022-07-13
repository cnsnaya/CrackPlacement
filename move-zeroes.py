#Link to the question:https://leetcode.com/problems/move-zeroes/

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        ctr = nums.count(0)
       
        nums[:] = (value for value in nums if value != 0)
        
        nums.extend([0]*ctr)
