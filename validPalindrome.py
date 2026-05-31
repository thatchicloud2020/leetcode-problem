class Solution:
    def isPalindrome(self, s: str) -> bool:
        result=s.lower()
        new_s=""
        
        for char in result:
            if char.isalnum():
                new_s +=char

        return new_s == new_s[::-1]
