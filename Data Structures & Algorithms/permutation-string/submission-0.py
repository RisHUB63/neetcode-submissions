class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        start = 0
        end = len(s1) - 1

        new_s1 = sorted(s1)



        while end < len(s2):
            new_s2 = sorted(s2[start:end+1])
            if new_s1 == new_s2:
                return True
            
            start += 1
            end += 1
        
        return False
