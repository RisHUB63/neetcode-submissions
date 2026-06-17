class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        answer = []

        for i in range(len(nums)):
            mem = set()
            for j in range(i+1, len(nums)):
                if -(nums[i] + nums[j]) in mem:
                    a = sorted([nums[i], -(nums[i] + nums[j]), nums[j]])
                    if a not in answer:
                        answer.append(a)
                else:
                    mem.add(nums[j])
        return answer
