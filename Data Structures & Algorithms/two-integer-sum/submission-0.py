class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        trace = {}
        for i in range(len(nums)):
            if target-nums[i] in trace:
                return [trace[target-nums[i]], i]
            trace[nums[i]] = i
        return [-1,-1]
        