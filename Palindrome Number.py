class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        return str(x)==str(x)[::-1]
        
        
def checkPalindrome(str):

    # check if str[i] is same as str[len(str) - i - 1]
    # for whole string
    for i in range(0, len(str)):

        # Basically, we are checking i-th character is
        # same as i-th character from the end or not
        if str[i] != str[len(str) - i - 1]:
            return False

    return True


num = 1234#int(input("enter a number"))
reverse = int(str(num)[::-1])

if num == reverse:
  print('Palindrome')
else:
  print("Not Palindrome")
