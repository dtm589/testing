'''
You are given an integer n and an integer start.

Define an array nums where nums[i] = start + 2 * i (0-indexed) and n == nums.length.

Return the bitwise XOR of all elements of nums.
'''


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = []
        output = 0
        for i in range(0, n):
            new_num = start + 2 * i
            nums.append(new_num)
        for i in range(0, n):
            output = output ^ nums[i]
        
        return output