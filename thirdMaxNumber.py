'''
Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.
'''

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        sorted_nums = sorted(set(nums), reverse=True)
        if len(sorted_nums) < 3:
            return sorted_nums[0]
        else:
            return sorted_nums[2]