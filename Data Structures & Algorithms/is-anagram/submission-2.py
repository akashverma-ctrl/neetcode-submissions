class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def signature(s):
            counts = [0] * 26
            for c in s:
                counts[ord(c) - ord('a')] += 1
            return tuple(counts)
        return signature(s) == signature(t)