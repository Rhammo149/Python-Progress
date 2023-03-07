class Solution:
    
    
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        reversed_x = 0
        original_x = x
        while x > 0:
            digit = x % 10
            reversed_x = reversed_x * 10 + digit
            x //= 10
        return reversed_x == original_x

s = Solution()
result = s.isPalindrome(12321)
print(result)
    
    
    
