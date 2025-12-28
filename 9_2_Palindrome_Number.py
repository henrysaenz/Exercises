"""Given an integer x, return true if x is a palindrome, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-2**31 <= x <= 2**31 - 1

"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        vector = [int(d) for d in str(x)] #list(map(int, str(x)))
        n = len(vector)
        m = n//2
        for i in range(m):
            if vector[i] - vector[n-1-i] ==0:
                m=m-1
        if m == 0:
            return True
        else:
            return False
            
sol = Solution()
print(sol.isPalindrome(24482))