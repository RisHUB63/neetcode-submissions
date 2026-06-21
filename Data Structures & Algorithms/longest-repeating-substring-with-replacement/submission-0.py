class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        maxF = 0
        l = 0
        for r in range(len(s)):
            count[s[r]] += 1
            maxF = max(maxF, count[s[r]])
            if (r-l+1) - maxF > k:
                count[s[l]] -= 1
                l += 1
        return r-l+1