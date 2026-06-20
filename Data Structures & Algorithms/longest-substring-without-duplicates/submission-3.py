class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        if len(s) < 2:
            return len(s)
        
        for i in range(len(s)):
            longest = ""
            j = i
            while j < len(s) and s[j] not in longest:
                longest += s[j]
                j+=1
            
            max_len = max(max_len, len(longest))
        return max_len