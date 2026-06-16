class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(' ', '').lower()
        start, end = 0, len(s)-1

        if len(s) == 1:
            return True

        while start < end:
            if not s[start].isalnum():
                start += 1
            elif not s[end].isalnum():
                end -= 1
            elif s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return False
        return True