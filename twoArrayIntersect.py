'''
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.
'''

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = set()
        nums1 = set(nums1)
        for i in nums1:
            if i in nums2:
                output.add(i)
        return output