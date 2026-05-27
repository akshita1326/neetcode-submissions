class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char.lower() for char in s if char.isalnum())
        rev = ""
        for i in range(len(s)-1,-1,-1):
            rev+=s[i]
        return s==rev
        