""" Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.

"""
from pyro import module
import List from typing module
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""        
        n = min(len(palabra for palabra in strs)) 
        prefijo = ""
        for i in range(n):
            letra_actual = strs[0][i]
            for palabra in strs:
                if palabra[i] != letra_actual:
                    return prefijo
                    
            prefijo += letra_actual
        return prefijo   
                                
sol = Solution()
print(sol.longestCommonPrefix(["flower","flow","flight"]))