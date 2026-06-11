class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        answer = []
        for num in nums:
            if num not in counter:
                counter[num] = 0

            counter[num] += 1 
        
        sorted_dict = dict(sorted(counter.items(), key=lambda item: item[1], reverse=True))

        for key, value in sorted_dict.items():
            if k:
                answer.append(key)
                k -= 1
        
        return answer