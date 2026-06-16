class Solution:
    def twoSum(self, number: List[int], target: int) -> List[int]:

        start, end = 0, len(number) -1

        while start < end:

            if number[start] + number[end] == target:
                return [start+1, end+1]
            
            elif number[start] + number[end] > target:
                end -= 1
            else:
                start += 1
        
        return [-1,-1]