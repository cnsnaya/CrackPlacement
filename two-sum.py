#Link to the question:https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lst = []
        #j = len(nums) - 1
        for i in range(len(nums)):
            j = len(nums) - 1
            while (i < j):
                
                sum = nums[i] + nums[j]
                if sum == target:
                    lst.append(i)
                    lst.append(j)
                j -= 1
            
              
        return lst  
