class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        letters = set(nums)
        if len(nums) == len(letters):
            return False 
        else:
            return True
        
        