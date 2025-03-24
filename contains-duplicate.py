class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        uniqueNums = set(nums)
        print(uniqueNums)
        if len(uniqueNums) == len(nums):
            return False
        else:
            return True
