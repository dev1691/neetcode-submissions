class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrmap={}
        for wrd in strs:
            key = list(wrd)
            key.sort()
            key = ''.join(key)
            if key not in anagrmap:
                anagrmap[key]=[wrd]
            else:
                anagrmap[key].append(wrd)
        return list(anagrmap.values())
