class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l = r = 0
        longestSubArray = 0
        subArray = set()
            
        while l <= r and r < len(s):
            if s[r] not in subArray:
                subArray.add(s[r])
                longestSubArray = max(longestSubArray, r-l+1)
                r+=1
            else:
                subArray.remove(s[l])
                l+=1
        return longestSubArray