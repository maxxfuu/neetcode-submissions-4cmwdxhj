class Solution:
    def isPalindrome(self, s: str) -> bool:
        palindrome = ""
        for char in s:
            if char.isalnum():
                palindrome += char.lower()
        print(palindrome)
        return True if palindrome == palindrome[::-1] else False