'''
Given two arrays of strings list1 and list2, find the common strings with the least index sum.

A common string is a string that appeared in both list1 and list2.

A common string with the least index sum is a common string such that if it appeared at list1[i] and list2[j] then i + j should be the minimum value among all the other common strings.

Return all the common strings with the least index sum. Return the answer in any order.
'''


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        length = len(list1) + len(list2)
        result = []
    
        for i, word1 in enumerate(list1):
            for j, word2 in enumerate(list2):
                if word1 == word2:
                    index_sum = i + j
                    if index_sum <= length:
                        if result == None:
                            result.append(word2)
                        elif length == index_sum:
                            result.append(word2)
                        else:
                            result = []
                            result.append(word2)

                        length = i+j
        return result