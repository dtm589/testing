'''
Given a 0-indexed integer array nums of length n and an integer target, return the number of pairs (i, j) where 0 <= i < j < n and nums[i] + nums[j] < target.
'''

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        output = 0
        for i, num in enumerate(nums):
            for j, num in enumerate(nums):
                if i < j and nums[i] + nums[j] < target:
                    output += 1

        return output