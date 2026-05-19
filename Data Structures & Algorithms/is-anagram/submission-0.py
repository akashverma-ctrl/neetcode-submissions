class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        result = {}
        for c in s:
            result[c] = result.get(c, 0) + 1
        
        for c in t:
            if c not in result:
                return False
            result[c] -= 1
        
        for count in result.values():
            if count:
                return False
        return True