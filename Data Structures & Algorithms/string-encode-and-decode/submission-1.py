class Solution:
    def encode(self, strs: List[str]) -> str:

        if len(strs) == 0:
            return ""
        
        return str(strs)

    def decode(self, s: str) -> List[str]:

        if s == "":
            return []
        
        return eval(s)
