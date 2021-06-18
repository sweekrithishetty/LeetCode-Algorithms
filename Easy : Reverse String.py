#Write a function that reverses a string. The input string is given as an array of characters s.
->Example 1:
  Input: s = ["h","e","l","l","o"]
  Output: ["o","l","l","e","h"]

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
#Different Approach
# Extended Slicing           
 Input = "Hello"
 print(Input[-1::-1]) #[start:stop:step]
#Using for loop
Input = "Hello"
result = ''
#Run a loop from len(str)-1 to 0
#one by one append characters fron end to start
# in result string
for i in range(len(Input)-1,-1,-1):
    result = result + Input[i] 
print(result)
#Using reverese function
Input = "Hello"
#It will reverse string in reverese  order 
reveresed = reversed(Input)
print(''.join(reveresed))

   
          
