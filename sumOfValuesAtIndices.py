'''
You are given a 0-indexed integer array nums and an integer k.

Return an integer that denotes the sum of elements in nums whose corresponding indices have exactly k set bits in their binary representation.

The set bits in an integer are the 1's present when it is written in binary.

For example, the binary representation of 21 is 10101, which has 3 set bits.
'''

class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        result = 0

        # Iterate through nums
        for i in range(0, len(nums)):
            # Convert the number to its binary representation as a string
            binary_rep = bin(i)[2:]

            # Count the number of set bits
            set_bits_count = str(binary_rep).count('1')

            # If the count is equal to k, add the num to the result
            if set_bits_count == k:
                result += nums[i]

        return result