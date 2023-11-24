'''
Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.
'''

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        string1 = ''
        string2 = ''
        for string in word1:
            string1 += string
        for string in word2:
            string2 += string
        if string1 == string2:
            return True
        return False