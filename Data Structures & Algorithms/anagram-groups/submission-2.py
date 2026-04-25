class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for i in strs:
            hh = sum(hash(j) for j in i)
            ans.setdefault(hh, []).append(i)
        return list(ans.values())
        