class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def signature(s):
            counts = [0] * 26
            for c in s:
                counts[ord(c) - ord('a')] += 1
            return tuple(counts)
        
        grp_anagrams = []
        for s in strs:
            element_inserted = False
            for i in range(len(grp_anagrams)):
                if signature(s) == signature(grp_anagrams[i][0]):
                    grp_anagrams[i].append(s)
                    element_inserted = True
            if not element_inserted:
                grp_anagrams.append([s])
        return grp_anagrams
