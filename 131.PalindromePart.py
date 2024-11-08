class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        result = []

        def createPartition(index, curr):
            if index == len(s):
                result.append(curr[:])
                return
            else:
                for i in range(index, len(s)):
                    substring = s[index:i+1]

                    if substring == substring[::-1]:
                        curr.append(substring)
                        createPartition(i + 1, curr)
                        curr.pop()
        
        createPartition(0, [])


        return result

s = Solution()
print(s.partition("aab")) # [["a", "a", "b"], ["aa", "b"]]


#Time Complexity: O(n * 2^n)
#Space Complexity: O(n)