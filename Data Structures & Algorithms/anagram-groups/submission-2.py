from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs: 
            an = "".join(sorted(s)) 
            groups[an].append(s)
        return list(groups.values())