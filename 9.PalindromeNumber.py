class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if (x < 0):
            return False
        temp = x
        reverse = 0
        while(temp != 0):
            remainder = temp % 10
            reverse = reverse * 10 + remainder
            temp = temp//10
    
        return reverse == x
        