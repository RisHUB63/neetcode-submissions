class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        if len(nums_set) < 2:
            return len(nums_set)

        longest = 0
        for num in nums_set:
            length = 0
            current = num

            while current in nums_set:
                length += 1
                current += 1

            longest = max(longest, length)
        return longest
                

