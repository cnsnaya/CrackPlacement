#Link of the question:https://leetcode.com/problems/find-the-duplicate-number/

class Solution(object):
    def findDuplicate(self, nums):
        count = {}
        for i in nums:
            count[i] = count.get(i, 0) + 1
        for key,value in count.items():
            if value>=2:
                return key
