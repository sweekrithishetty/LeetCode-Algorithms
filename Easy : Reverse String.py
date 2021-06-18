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
        
