"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
"""
#Time O(n), Space O(1) 
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        steps_needed = len(nums)
        steps_allowed = -1
        
        for i in range(len(nums)):
            if nums[i] >= steps_allowed:
                steps_allowed = nums[i]
            else:
                steps_allowed -= 1
            
            steps_needed -= 1

            if steps_allowed >= steps_needed:
                return True
            
            if steps_allowed == 0:
                return False
