class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        answer = []
        i = 0
        while i < len(nums):
            multiple = 1
            for j in range(len(nums)):
                if i != j:
                    multiple *= nums[j]

            answer.append(multiple)
            i += 1

        return answer
