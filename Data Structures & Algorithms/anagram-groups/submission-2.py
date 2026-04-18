class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grps={}
        for s in strs:
            key = ''.join(sorted(s))
            if key in grps:
                grps[key].append(s)
            elif key not in grps:
                grps[key]=[s]
        return list(grps.values())

        