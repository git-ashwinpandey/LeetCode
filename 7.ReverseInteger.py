"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-231 <= x <= 231 - 1
"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = False
        temp = x
        if (x < 0):
            negative = True
            temp = temp * -1
            
        
        reverse = 0
        while(temp != 0):
            remainder = temp % 10
            reverse = reverse * 10 + remainder
            temp = temp//10

        if negative:
            reverse = -1 * reverse


        if -2**31 <= reverse <= 2**31 - 1:
            return reverse
        return 0
    

temp = Solution()
test = temp.reverse(1534236469)
print(test)