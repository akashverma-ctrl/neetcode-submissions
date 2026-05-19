class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def is_anagram(s, t):
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
        
        grp_anagrams = []
        for s in strs:
            element_inserted = False
            for i in range(len(grp_anagrams)):
                if is_anagram(s, grp_anagrams[i][0]):
                    grp_anagrams[i].append(s)
                    element_inserted = True
            if not element_inserted:
                grp_anagrams.append([s])
        return grp_anagrams
