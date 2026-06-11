class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        answer = []
        track = {}

        for words in strs:
            sort = "".join(sorted(words))

            if sort not in track:
                track[sort] = []
            
            track[sort].append(words)
        


        for word in track.values():
            answer.append(word)
        
        return answer