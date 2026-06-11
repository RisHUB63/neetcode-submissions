class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letter = {}
        for char in s:
            if char not in letter:
                letter[char] = 0
            letter[char] += 1
        print(letter)
        for char in t:
            if char not in letter:
                return False
            letter[char] -= 1

            if letter[char] == 0:
                letter.pop(char)
        
        if len(letter) > 0:
            return False
        return True

        