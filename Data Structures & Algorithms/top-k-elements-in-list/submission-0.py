class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        ans = [i for i, j in sorted(list(freq.items()), key = lambda x: x[1], reverse=True)]
        return ans[0:k]