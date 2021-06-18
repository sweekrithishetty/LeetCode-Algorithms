#Write a function that reverses a string. The input string is given as an array of characters s.

 #Example 1:

#Input: s = ["h","e","l","l","o"]
#Output: ["o","l","l","e","h"]

class Solution:
    def reverseString(self, s):
        left = 0;
        right = len(s) - 1
        while(left < right):
            temp = s[left]
            s[left] = s[right]
            left += 1
            s[right] = temp
            right -= 1
        
