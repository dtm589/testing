'''
You are given a positive integer num consisting of exactly four digits. Split num into two new integers new1 and new2 by using the digits found in num. Leading zeros are allowed in new1 and new2, and all the digits found in num must be used.

For example, given num = 2932, you have the following digits: two 2's, one 9 and one 3. Some of the possible pairs [new1, new2] are [22, 93], [23, 92], [223, 9] and [2, 329].
Return the minimum possible sum of new1 and new2.
'''


class Solution:
    def minimumSum(self, num: int) -> int:
        #varaible to return
        min_sum = 0
        # sort a list of digits in descending order
        list_of_nums = sorted(str(num), reverse = True)
        even = False
        position = 0
        # iterate through the digits
        for num in list_of_nums:
            # * 10^positon
            min_sum += int(num) * (10**position)
            if even:
                position += 1
                even = False
            else:
                even = True

        return min_sum