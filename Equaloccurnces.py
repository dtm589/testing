'''
Given a string s, return true if s is a good string, or false otherwise.

A string s is good if all the characters that appear in s have the same number of occurrences (i.e., the same frequency).
'''

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counts = []
        for i in s:
            count = s.count(i)
            counts.append(count)
        if min(counts) == max(counts):
            return True
        return False