'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        newSet = set()
        for num in nums:
            if num in newSet:
                return True
            seen.add(num)
        return False