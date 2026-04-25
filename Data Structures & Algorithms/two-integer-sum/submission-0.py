class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_dict = {}
        for j,i in enumerate(nums):
            diff = target - i
            if diff in diff_dict:
                return [diff_dict[diff], j]
            diff_dict[i] = j