class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def generate_count_result(string):
            result = {}
            for c in string:
                result[c] = result.get(c, 0) + 1
            return result
        
        return generate_count_result(s) == generate_count_result(t)