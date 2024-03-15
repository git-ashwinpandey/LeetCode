"""
169. Majority Element
Solved
Easy
Topics
Companies
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
 

Follow-up: Could you solve the problem in linear time and in O(1) space?
"""
#Time O(n) Space O(n)
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        t_dict = defaultdict(int) 
        size = len(nums)
        target = size//2
        for i in range(size):
            t_dict[nums[i]] += 1

        for key, value in t_dict.items():
            if value > target:
                return key

#Boyer-Moore Algorithm
#Time O(n) Space O(1)
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        candidate = -1

        for i in range(len(nums)):
            if (count == 0):
                candidate = nums[i]
            if(nums[i] != candidate):
                count -= 1
            else:
                count += 1
                
        return candidate